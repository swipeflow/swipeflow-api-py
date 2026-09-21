from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.media_descriptor import MediaDescriptor
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/media-uploads/{id}/confirm".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | MediaDescriptor | None:
    if response.status_code == 200:
        response_200 = MediaDescriptor.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | MediaDescriptor]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | MediaDescriptor]:
    """Confirm a completed direct upload (step 2 of 2)

     Call after the direct-to-storage `PUT` completes. `HEAD`s the object, requires its actual size to
    equal the declared size, persists the opaque storage ETag, and moves the media to `uploaded`.
    Idempotent. A size mismatch fails completion, releases the reservation, and schedules the object for
    deletion. Returns the media record with a short-lived `contentUrl`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaDescriptor]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | MediaDescriptor | None:
    """Confirm a completed direct upload (step 2 of 2)

     Call after the direct-to-storage `PUT` completes. `HEAD`s the object, requires its actual size to
    equal the declared size, persists the opaque storage ETag, and moves the media to `uploaded`.
    Idempotent. A size mismatch fails completion, releases the reservation, and schedules the object for
    deletion. Returns the media record with a short-lived `contentUrl`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaDescriptor
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | MediaDescriptor]:
    """Confirm a completed direct upload (step 2 of 2)

     Call after the direct-to-storage `PUT` completes. `HEAD`s the object, requires its actual size to
    equal the declared size, persists the opaque storage ETag, and moves the media to `uploaded`.
    Idempotent. A size mismatch fails completion, releases the reservation, and schedules the object for
    deletion. Returns the media record with a short-lived `contentUrl`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MediaDescriptor]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | MediaDescriptor | None:
    """Confirm a completed direct upload (step 2 of 2)

     Call after the direct-to-storage `PUT` completes. `HEAD`s the object, requires its actual size to
    equal the declared size, persists the opaque storage ETag, and moves the media to `uploaded`.
    Idempotent. A size mismatch fails completion, releases the reservation, and schedules the object for
    deletion. Returns the media record with a short-lived `contentUrl`.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MediaDescriptor
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
