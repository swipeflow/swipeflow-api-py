from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_project_media_status import ListProjectMediaStatus
from ...models.media_list_page import MediaListPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListProjectMediaStatus | Unset = UNSET,
    attached: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["attached"] = attached

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/media".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MediaListPage | None:
    if response.status_code == 200:
        response_200 = MediaListPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MediaListPage]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListProjectMediaStatus | Unset = UNSET,
    attached: bool | Unset = UNSET,
) -> Response[Any | MediaListPage]:
    """List project media

     Cursor-paginated, newest first. Excludes `deleted` tombstones unless `status` explicitly asks for
    them. Every row's signed URL shares one absolute expiry.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        status (ListProjectMediaStatus | Unset):
        attached (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaListPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cursor=cursor,
        limit=limit,
        status=status,
        attached=attached,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListProjectMediaStatus | Unset = UNSET,
    attached: bool | Unset = UNSET,
) -> Any | MediaListPage | None:
    """List project media

     Cursor-paginated, newest first. Excludes `deleted` tombstones unless `status` explicitly asks for
    them. Every row's signed URL shares one absolute expiry.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        status (ListProjectMediaStatus | Unset):
        attached (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaListPage
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        cursor=cursor,
        limit=limit,
        status=status,
        attached=attached,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListProjectMediaStatus | Unset = UNSET,
    attached: bool | Unset = UNSET,
) -> Response[Any | MediaListPage]:
    """List project media

     Cursor-paginated, newest first. Excludes `deleted` tombstones unless `status` explicitly asks for
    them. Every row's signed URL shares one absolute expiry.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        status (ListProjectMediaStatus | Unset):
        attached (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaListPage]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cursor=cursor,
        limit=limit,
        status=status,
        attached=attached,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    status: ListProjectMediaStatus | Unset = UNSET,
    attached: bool | Unset = UNSET,
) -> Any | MediaListPage | None:
    """List project media

     Cursor-paginated, newest first. Excludes `deleted` tombstones unless `status` explicitly asks for
    them. Every row's signed URL shares one absolute expiry.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        status (ListProjectMediaStatus | Unset):
        attached (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaListPage
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            cursor=cursor,
            limit=limit,
            status=status,
            attached=attached,
        )
    ).parsed
