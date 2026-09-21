from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.item_status_snapshot_list import ItemStatusSnapshotList
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    ids: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/items/status".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ItemStatusSnapshotList | None:
    if response.status_code == 200:
        response_200 = ItemStatusSnapshotList.from_dict(response.json())

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
) -> Response[ErrorResponse | ItemStatusSnapshotList]:
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
    ids: str,
) -> Response[ErrorResponse | ItemStatusSnapshotList]:
    """Get slim status for multiple items

     Batch variant of the single-item status endpoint — one round trip for N items instead of N. Ids that
    don't exist or aren't in this project are silently omitted from the result rather than causing an
    error.

    Args:
        project_id (str):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemStatusSnapshotList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    ids: str,
) -> ErrorResponse | ItemStatusSnapshotList | None:
    """Get slim status for multiple items

     Batch variant of the single-item status endpoint — one round trip for N items instead of N. Ids that
    don't exist or aren't in this project are silently omitted from the result rather than causing an
    error.

    Args:
        project_id (str):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemStatusSnapshotList
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    ids: str,
) -> Response[ErrorResponse | ItemStatusSnapshotList]:
    """Get slim status for multiple items

     Batch variant of the single-item status endpoint — one round trip for N items instead of N. Ids that
    don't exist or aren't in this project are silently omitted from the result rather than causing an
    error.

    Args:
        project_id (str):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ItemStatusSnapshotList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    ids: str,
) -> ErrorResponse | ItemStatusSnapshotList | None:
    """Get slim status for multiple items

     Batch variant of the single-item status endpoint — one round trip for N items instead of N. Ids that
    don't exist or aren't in this project are silently omitted from the result rather than causing an
    error.

    Args:
        project_id (str):
        ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ItemStatusSnapshotList
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            ids=ids,
        )
    ).parsed
