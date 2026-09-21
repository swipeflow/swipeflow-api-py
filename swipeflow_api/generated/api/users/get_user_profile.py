from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.user_profile import UserProfile
from ...types import Response


def _get_kwargs(
    user_id_or_me: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id_or_me}/profile".format(
            user_id_or_me=quote(str(user_id_or_me), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UserProfile | None:
    if response.status_code == 200:
        response_200 = UserProfile.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | UserProfile]:
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
) -> Response[ErrorResponse | UserProfile]:
    """Get user profile

     Retrieve the current user's profile information

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UserProfile]
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
) -> ErrorResponse | UserProfile | None:
    """Get user profile

     Retrieve the current user's profile information

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UserProfile
    """

    return sync_detailed(
        user_id_or_me=user_id_or_me,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | UserProfile]:
    """Get user profile

     Retrieve the current user's profile information

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UserProfile]
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
) -> ErrorResponse | UserProfile | None:
    """Get user profile

     Retrieve the current user's profile information

    Args:
        user_id_or_me (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UserProfile
    """

    return (
        await asyncio_detailed(
            user_id_or_me=user_id_or_me,
            client=client,
        )
    ).parsed
