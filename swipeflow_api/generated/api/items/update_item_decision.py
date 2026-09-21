from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item import Item
from ...models.update_item_decision_request import UpdateItemDecisionRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    item_id: str,
    *,
    body: UpdateItemDecisionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/items/{item_id}/decision".format(
            project_id=quote(str(project_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Item | None:
    if response.status_code == 200:
        response_200 = Item.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | Item]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateItemDecisionRequest,
) -> Response[ErrorResponse | Item]:
    """Update item decision

     Update the decision status of an item. When decision is 'change_requested', a comment is required.

    Args:
        project_id (str):
        item_id (str):
        body (UpdateItemDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateItemDecisionRequest,
) -> ErrorResponse | Item | None:
    """Update item decision

     Update the decision status of an item. When decision is 'change_requested', a comment is required.

    Args:
        project_id (str):
        item_id (str):
        body (UpdateItemDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return sync_detailed(
        project_id=project_id,
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateItemDecisionRequest,
) -> Response[ErrorResponse | Item]:
    """Update item decision

     Update the decision status of an item. When decision is 'change_requested', a comment is required.

    Args:
        project_id (str):
        item_id (str):
        body (UpdateItemDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateItemDecisionRequest,
) -> ErrorResponse | Item | None:
    """Update item decision

     Update the decision status of an item. When decision is 'change_requested', a comment is required.

    Args:
        project_id (str):
        item_id (str):
        body (UpdateItemDecisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Item
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
