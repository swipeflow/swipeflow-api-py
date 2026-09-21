from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item_version_list import ItemVersionList
from ...models.list_item_versions_sort_order import ListItemVersionsSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    item_id: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    sort_order: ListItemVersionsSortOrder | Unset = ListItemVersionsSortOrder.DESC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/items/{item_id}/versions".format(
            project_id=quote(str(project_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ItemVersionList | None:
    if response.status_code == 200:
        response_200 = ItemVersionList.from_dict(response.json())

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
) -> Response[ErrorResponse | ItemVersionList]:
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
    page: int | Unset = 1,
    limit: int | Unset = 10,
    sort_order: ListItemVersionsSortOrder | Unset = ListItemVersionsSortOrder.DESC,
) -> Response[ErrorResponse | ItemVersionList]:
    """Get all versions for an item

     Retrieve all versions for a specific item with pagination

    Args:
        project_id (str):
        item_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        sort_order (ListItemVersionsSortOrder | Unset):  Default: ListItemVersionsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemVersionList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        page=page,
        limit=limit,
        sort_order=sort_order,
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
    page: int | Unset = 1,
    limit: int | Unset = 10,
    sort_order: ListItemVersionsSortOrder | Unset = ListItemVersionsSortOrder.DESC,
) -> ErrorResponse | ItemVersionList | None:
    """Get all versions for an item

     Retrieve all versions for a specific item with pagination

    Args:
        project_id (str):
        item_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        sort_order (ListItemVersionsSortOrder | Unset):  Default: ListItemVersionsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemVersionList
    """

    return sync_detailed(
        project_id=project_id,
        item_id=item_id,
        client=client,
        page=page,
        limit=limit,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    sort_order: ListItemVersionsSortOrder | Unset = ListItemVersionsSortOrder.DESC,
) -> Response[ErrorResponse | ItemVersionList]:
    """Get all versions for an item

     Retrieve all versions for a specific item with pagination

    Args:
        project_id (str):
        item_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        sort_order (ListItemVersionsSortOrder | Unset):  Default: ListItemVersionsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemVersionList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        page=page,
        limit=limit,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    sort_order: ListItemVersionsSortOrder | Unset = ListItemVersionsSortOrder.DESC,
) -> ErrorResponse | ItemVersionList | None:
    """Get all versions for an item

     Retrieve all versions for a specific item with pagination

    Args:
        project_id (str):
        item_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        sort_order (ListItemVersionsSortOrder | Unset):  Default: ListItemVersionsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemVersionList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            item_id=item_id,
            client=client,
            page=page,
            limit=limit,
            sort_order=sort_order,
        )
    ).parsed
