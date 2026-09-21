from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_storage_use_response_200 import GetUserStorageUseResponse200
from ...types import Response


def _get_kwargs(
    user_id_or_me: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id_or_me}/storage-use".format(
            user_id_or_me=quote(str(user_id_or_me), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetUserStorageUseResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUserStorageUseResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetUserStorageUseResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GetUserStorageUseResponse200]:
    """Combined storage allowance and usage across every owned project

     `limitBytes`/`plan`/`seats` are the user's combined plan quota (free allowance, or pro allowance ×
    seats). `usedBytes` is the total across every project this user owns. `media` breaks that total down
    per project — other consumers of the same quota may join this response later.

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserStorageUseResponse200]
    """

    kwargs = _get_kwargs(
        user_id_or_me=user_id_or_me,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
) -> Any | GetUserStorageUseResponse200 | None:
    """Combined storage allowance and usage across every owned project

     `limitBytes`/`plan`/`seats` are the user's combined plan quota (free allowance, or pro allowance ×
    seats). `usedBytes` is the total across every project this user owns. `media` breaks that total down
    per project — other consumers of the same quota may join this response later.

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserStorageUseResponse200
    """

    return sync_detailed(
        user_id_or_me=user_id_or_me,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GetUserStorageUseResponse200]:
    """Combined storage allowance and usage across every owned project

     `limitBytes`/`plan`/`seats` are the user's combined plan quota (free allowance, or pro allowance ×
    seats). `usedBytes` is the total across every project this user owns. `media` breaks that total down
    per project — other consumers of the same quota may join this response later.

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUserStorageUseResponse200]
    """

    kwargs = _get_kwargs(
        user_id_or_me=user_id_or_me,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
) -> Any | GetUserStorageUseResponse200 | None:
    """Combined storage allowance and usage across every owned project

     `limitBytes`/`plan`/`seats` are the user's combined plan quota (free allowance, or pro allowance ×
    seats). `usedBytes` is the total across every project this user owns. `media` breaks that total down
    per project — other consumers of the same quota may join this response later.

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUserStorageUseResponse200
    """

    return (
        await asyncio_detailed(
            user_id_or_me=user_id_or_me,
            client=client,
        )
    ).parsed
