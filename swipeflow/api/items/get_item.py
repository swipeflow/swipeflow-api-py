from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item import Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    item_id: str,
    *,
    include_versions: bool | Unset = False,
    resolve_media: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeVersions"] = include_versions

    params["resolveMedia"] = resolve_media

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/items/{item_id}".format(
            project_id=quote(str(project_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Item | None:
    if response.status_code == 200:
        response_200 = Item.from_dict(response.json())

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
    include_versions: bool | Unset = False,
    resolve_media: bool | Unset = False,
) -> Response[ErrorResponse | Item]:
    """Get a specific item

     Retrieve details of a specific item, optionally including all revisions

    Args:
        project_id (str):
        item_id (str):
        include_versions (bool | Unset):  Default: False.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        include_versions=include_versions,
        resolve_media=resolve_media,
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
    include_versions: bool | Unset = False,
    resolve_media: bool | Unset = False,
) -> ErrorResponse | Item | None:
    """Get a specific item

     Retrieve details of a specific item, optionally including all revisions

    Args:
        project_id (str):
        item_id (str):
        include_versions (bool | Unset):  Default: False.
        resolve_media (bool | Unset):  Default: False.

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
        include_versions=include_versions,
        resolve_media=resolve_media,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    include_versions: bool | Unset = False,
    resolve_media: bool | Unset = False,
) -> Response[ErrorResponse | Item]:
    """Get a specific item

     Retrieve details of a specific item, optionally including all revisions

    Args:
        project_id (str):
        item_id (str):
        include_versions (bool | Unset):  Default: False.
        resolve_media (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Item]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        item_id=item_id,
        include_versions=include_versions,
        resolve_media=resolve_media,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    include_versions: bool | Unset = False,
    resolve_media: bool | Unset = False,
) -> ErrorResponse | Item | None:
    """Get a specific item

     Retrieve details of a specific item, optionally including all revisions

    Args:
        project_id (str):
        item_id (str):
        include_versions (bool | Unset):  Default: False.
        resolve_media (bool | Unset):  Default: False.

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
            include_versions=include_versions,
            resolve_media=resolve_media,
        )
    ).parsed
