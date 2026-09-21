from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item_list import ItemList
from ...models.list_items_sort_by import ListItemsSortBy
from ...models.list_items_sort_order import ListItemsSortOrder
from ...models.list_items_status import ListItemsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    status: ListItemsStatus | Unset = UNSET,
    processed: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListItemsSortBy | Unset = UNSET,
    sort_order: ListItemsSortOrder | Unset = ListItemsSortOrder.DESC,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    resolve_media: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["processed"] = processed

    params["search"] = search

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["page"] = page

    params["limit"] = limit

    params["resolveMedia"] = resolve_media

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/items".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ItemList | None:
    if response.status_code == 200:
        response_200 = ItemList.from_dict(response.json())

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
) -> Response[ErrorResponse | ItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListItemsStatus | Unset = UNSET,
    processed: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListItemsSortBy | Unset = UNSET,
    sort_order: ListItemsSortOrder | Unset = ListItemsSortOrder.DESC,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    resolve_media: bool | Unset = False,
) -> Response[ErrorResponse | ItemList]:
    """Get all items

     Retrieve all items for a specific project

    Args:
        project_id (str):
        status (ListItemsStatus | Unset):
        processed (bool | Unset):
        search (str | Unset):
        sort_by (ListItemsSortBy | Unset):
        sort_order (ListItemsSortOrder | Unset):  Default: ListItemsSortOrder.DESC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        status=status,
        processed=processed,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        limit=limit,
        resolve_media=resolve_media,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListItemsStatus | Unset = UNSET,
    processed: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListItemsSortBy | Unset = UNSET,
    sort_order: ListItemsSortOrder | Unset = ListItemsSortOrder.DESC,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    resolve_media: bool | Unset = False,
) -> ErrorResponse | ItemList | None:
    """Get all items

     Retrieve all items for a specific project

    Args:
        project_id (str):
        status (ListItemsStatus | Unset):
        processed (bool | Unset):
        search (str | Unset):
        sort_by (ListItemsSortBy | Unset):
        sort_order (ListItemsSortOrder | Unset):  Default: ListItemsSortOrder.DESC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        status=status,
        processed=processed,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        limit=limit,
        resolve_media=resolve_media,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListItemsStatus | Unset = UNSET,
    processed: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListItemsSortBy | Unset = UNSET,
    sort_order: ListItemsSortOrder | Unset = ListItemsSortOrder.DESC,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    resolve_media: bool | Unset = False,
) -> Response[ErrorResponse | ItemList]:
    """Get all items

     Retrieve all items for a specific project

    Args:
        project_id (str):
        status (ListItemsStatus | Unset):
        processed (bool | Unset):
        search (str | Unset):
        sort_by (ListItemsSortBy | Unset):
        sort_order (ListItemsSortOrder | Unset):  Default: ListItemsSortOrder.DESC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        status=status,
        processed=processed,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        limit=limit,
        resolve_media=resolve_media,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    status: ListItemsStatus | Unset = UNSET,
    processed: bool | Unset = UNSET,
    search: str | Unset = UNSET,
    sort_by: ListItemsSortBy | Unset = UNSET,
    sort_order: ListItemsSortOrder | Unset = ListItemsSortOrder.DESC,
    page: int | Unset = 1,
    limit: int | Unset = 10,
    resolve_media: bool | Unset = False,
) -> ErrorResponse | ItemList | None:
    """Get all items

     Retrieve all items for a specific project

    Args:
        project_id (str):
        status (ListItemsStatus | Unset):
        processed (bool | Unset):
        search (str | Unset):
        sort_by (ListItemsSortBy | Unset):
        sort_order (ListItemsSortOrder | Unset):  Default: ListItemsSortOrder.DESC.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            status=status,
            processed=processed,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            limit=limit,
            resolve_media=resolve_media,
        )
    ).parsed
