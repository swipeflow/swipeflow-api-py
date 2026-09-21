from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.run_trigger_request import RunTriggerRequest
from ...models.run_trigger_response_200 import RunTriggerResponse200
from ...types import Response


def _get_kwargs(
    project_id: str,
    trigger_id: str,
    *,
    body: RunTriggerRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/triggers/{trigger_id}/run".format(
            project_id=quote(str(project_id), safe=""),
            trigger_id=quote(str(trigger_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RunTriggerResponse200 | None:
    if response.status_code == 200:
        response_200 = RunTriggerResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | RunTriggerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient,
    body: RunTriggerRequest,
) -> Response[ErrorResponse | RunTriggerResponse200]:
    """Run a project trigger

     Executes a manual trigger defined in the project's trigger configuration and sends the associated
    webhook.

    Args:
        project_id (str):
        trigger_id (str):
        body (RunTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RunTriggerResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        trigger_id=trigger_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient,
    body: RunTriggerRequest,
) -> ErrorResponse | RunTriggerResponse200 | None:
    """Run a project trigger

     Executes a manual trigger defined in the project's trigger configuration and sends the associated
    webhook.

    Args:
        project_id (str):
        trigger_id (str):
        body (RunTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RunTriggerResponse200
    """

    return sync_detailed(
        project_id=project_id,
        trigger_id=trigger_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient,
    body: RunTriggerRequest,
) -> Response[ErrorResponse | RunTriggerResponse200]:
    """Run a project trigger

     Executes a manual trigger defined in the project's trigger configuration and sends the associated
    webhook.

    Args:
        project_id (str):
        trigger_id (str):
        body (RunTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RunTriggerResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        trigger_id=trigger_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    trigger_id: str,
    *,
    client: AuthenticatedClient,
    body: RunTriggerRequest,
) -> ErrorResponse | RunTriggerResponse200 | None:
    """Run a project trigger

     Executes a manual trigger defined in the project's trigger configuration and sends the associated
    webhook.

    Args:
        project_id (str):
        trigger_id (str):
        body (RunTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RunTriggerResponse200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            trigger_id=trigger_id,
            client=client,
            body=body,
        )
    ).parsed
