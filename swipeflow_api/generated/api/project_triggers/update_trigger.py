from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.project_trigger import ProjectTrigger
from ...models.update_trigger_request import UpdateTriggerRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    trigger_id: str,
    *,
    body: UpdateTriggerRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/triggers/{trigger_id}".format(
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
) -> ErrorResponse | ProjectTrigger | None:
    if response.status_code == 200:
        response_200 = ProjectTrigger.from_dict(response.json())

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
) -> Response[ErrorResponse | ProjectTrigger]:
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
    body: UpdateTriggerRequest,
) -> Response[ErrorResponse | ProjectTrigger]:
    """Update manual trigger

     Update an existing manual trigger

    Args:
        project_id (str):
        trigger_id (str):
        body (UpdateTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectTrigger]
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
    body: UpdateTriggerRequest,
) -> ErrorResponse | ProjectTrigger | None:
    """Update manual trigger

     Update an existing manual trigger

    Args:
        project_id (str):
        trigger_id (str):
        body (UpdateTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectTrigger
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
    body: UpdateTriggerRequest,
) -> Response[ErrorResponse | ProjectTrigger]:
    """Update manual trigger

     Update an existing manual trigger

    Args:
        project_id (str):
        trigger_id (str):
        body (UpdateTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectTrigger]
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
    body: UpdateTriggerRequest,
) -> ErrorResponse | ProjectTrigger | None:
    """Update manual trigger

     Update an existing manual trigger

    Args:
        project_id (str):
        trigger_id (str):
        body (UpdateTriggerRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectTrigger
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            trigger_id=trigger_id,
            client=client,
            body=body,
        )
    ).parsed
