import asyncio

import httpx
import pytest

from swipeflow import DEFAULT_BASE_URL, SwipeFlowClient, SwipeFlowError
from swipeflow.api.billing import get_billing
from swipeflow.api.projects import get_project, list_projects
from swipeflow.models import ProjectList


def make_client(handler, **kwargs):
    return SwipeFlowClient(httpx_args={"transport": httpx.MockTransport(handler)}, **kwargs)


def test_api_key_is_sent_as_x_api_key_header():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["headers"] = request.headers
        seen["url"] = str(request.url)
        return httpx.Response(200, json={"projects": []})

    with make_client(handler, api_key="secret") as client:
        result = list_projects.sync(client=client)

    assert isinstance(result, ProjectList)
    assert seen["headers"]["x-api-key"] == "secret"
    assert "authorization" not in seen["headers"]
    assert seen["url"].startswith(f"{DEFAULT_BASE_URL}/v1/projects")


def test_api_key_falls_back_to_environment(monkeypatch):
    monkeypatch.setenv("SWIPEFLOW_API_KEY", "from-env")
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["key"] = request.headers.get("x-api-key")
        return httpx.Response(200, json={"projects": []})

    with make_client(handler) as client:
        list_projects.sync(client=client)

    assert seen["key"] == "from-env"


def test_missing_credentials_raise_value_error(monkeypatch):
    monkeypatch.delenv("SWIPEFLOW_API_KEY", raising=False)
    with pytest.raises(ValueError, match="SWIPEFLOW_API_KEY"):
        SwipeFlowClient()


def test_token_is_sent_as_bearer_authorization():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["headers"] = request.headers
        return httpx.Response(200, json={"projects": []})

    with make_client(handler, token="jwt") as client:
        list_projects.sync(client=client)

    assert seen["headers"]["authorization"] == "Bearer jwt"
    assert "x-api-key" not in seen["headers"]


def test_http_errors_raise_swipeflow_error_with_server_message():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"message": "Project not found"})

    with make_client(handler, api_key="k") as client:
        with pytest.raises(SwipeFlowError) as excinfo:
            get_project.sync(project_id="p1", client=client)

    assert excinfo.value.status_code == 404
    assert excinfo.value.message == "Project not found"
    assert str(excinfo.value) == "404 Project not found"


def test_validation_errors_are_exposed():
    field_errors = [{"field": "name", "message": "required"}]

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"message": "Invalid", "errors": field_errors})

    with make_client(handler, api_key="k") as client:
        with pytest.raises(SwipeFlowError) as excinfo:
            list_projects.sync(client=client)

    assert excinfo.value.errors == field_errors


def test_error_field_is_used_when_the_body_has_no_message():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"error": "Invalid projectId"})

    with make_client(handler, api_key="k") as client:
        with pytest.raises(SwipeFlowError) as excinfo:
            get_project.sync(project_id="x", client=client)

    assert excinfo.value.status_code == 400
    assert excinfo.value.message == "Invalid projectId"


def test_non_json_error_bodies_fall_back_to_reason_phrase():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(502, text="<html>bad gateway</html>")

    with make_client(handler, api_key="k") as client:
        with pytest.raises(SwipeFlowError) as excinfo:
            list_projects.sync(client=client)

    assert excinfo.value.status_code == 502
    assert excinfo.value.body is None
    assert excinfo.value.message == "Bad Gateway"


def test_async_http_errors_raise_swipeflow_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"message": "Unauthorized"})

    async def run():
        async with make_client(handler, api_key="k") as client:
            await list_projects.asyncio(client=client)

    with pytest.raises(SwipeFlowError) as excinfo:
        asyncio.run(run())

    assert excinfo.value.status_code == 401


def test_derived_clients_keep_auth_and_error_handling():
    def failing(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"message": "boom"})

    derived = make_client(failing, api_key="k").with_headers({"X-Extra": "1"})

    assert isinstance(derived, SwipeFlowClient)
    with derived:
        with pytest.raises(SwipeFlowError):
            list_projects.sync(client=derived)


def test_endpoint_functions_can_be_imported_directly():
    from swipeflow.api.projects.list_projects import asyncio as list_projects_async
    from swipeflow.api.projects.list_projects import sync as list_projects_sync

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"projects": []})

    async def run():
        async with make_client(handler, api_key="k") as client:
            return await list_projects_async(client=client)

    with make_client(handler, api_key="k") as client:
        assert isinstance(list_projects_sync(client=client), ProjectList)
    assert isinstance(asyncio.run(run()), ProjectList)


def test_endpoints_without_response_schema_expose_raw_content():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"plan": "free"})

    with make_client(handler, api_key="k") as client:
        response = get_billing.sync_detailed(client=client)

    assert response.status_code == 200
    assert response.content == b'{"plan":"free"}'
