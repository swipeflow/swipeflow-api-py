from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item_status_snapshot import ItemStatusSnapshot
from ...types import Response


def _get_kwargs(
    project_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/items/{item_id}/status".format(
            project_id=quote(str(project_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ItemStatusSnapshot | None:
    if response.status_code == 200:
        response_200 = ItemStatusSnapshot.from_dict(response.json())

        return response_200

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
) -> Response[ErrorResponse | ItemStatusSnapshot]:
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
) -> Response[ErrorResponse | ItemStatusSnapshot]:
    """Get slim status for an item

     Returns only status, version, and the latest decision — not content or metadata. The cheap
    alternative to GET /:itemId when polling for a decision.

    Args:
        project_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemStatusSnapshot]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
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
) -> ErrorResponse | ItemStatusSnapshot | None:
    """Get slim status for an item

     Returns only status, version, and the latest decision — not content or metadata. The cheap
    alternative to GET /:itemId when polling for a decision.

    Args:
        project_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemStatusSnapshot
    """

    return sync_detailed(
        project_id=project_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ItemStatusSnapshot]:
    """Get slim status for an item

     Returns only status, version, and the latest decision — not content or metadata. The cheap
    alternative to GET /:itemId when polling for a decision.

    Args:
        project_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemStatusSnapshot]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ItemStatusSnapshot | None:
    """Get slim status for an item

     Returns only status, version, and the latest decision — not content or metadata. The cheap
    alternative to GET /:itemId when polling for a decision.

    Args:
        project_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemStatusSnapshot
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
