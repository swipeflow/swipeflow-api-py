from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_profile_picture import UpdateProfilePicture
from ...models.update_user_profile_picture_body import UpdateUserProfilePictureBody
from ...types import Response


def _get_kwargs(
    user_id_or_me: str,
    *,
    body: UpdateUserProfilePictureBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/users/{user_id_or_me}/profile-picture".format(
            user_id_or_me=quote(str(user_id_or_me), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | UpdateProfilePicture | None:
    if response.status_code == 200:
        response_200 = UpdateProfilePicture.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[ErrorResponse | UpdateProfilePicture]:
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
    body: UpdateUserProfilePictureBody,
) -> Response[ErrorResponse | UpdateProfilePicture]:
    """Update profile picture

     Upload a new profile picture

    Args:
        user_id_or_me (str):
        body (UpdateUserProfilePictureBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateProfilePicture]
    """

    kwargs = _get_kwargs(
        user_id_or_me=user_id_or_me,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserProfilePictureBody,
) -> ErrorResponse | UpdateProfilePicture | None:
    """Update profile picture

     Upload a new profile picture

    Args:
        user_id_or_me (str):
        body (UpdateUserProfilePictureBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateProfilePicture
    """

    return sync_detailed(
        user_id_or_me=user_id_or_me,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserProfilePictureBody,
) -> Response[ErrorResponse | UpdateProfilePicture]:
    """Update profile picture

     Upload a new profile picture

    Args:
        user_id_or_me (str):
        body (UpdateUserProfilePictureBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | UpdateProfilePicture]
    """

    kwargs = _get_kwargs(
        user_id_or_me=user_id_or_me,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id_or_me: str,
    *,
    client: AuthenticatedClient,
    body: UpdateUserProfilePictureBody,
) -> ErrorResponse | UpdateProfilePicture | None:
    """Update profile picture

     Upload a new profile picture

    Args:
        user_id_or_me (str):
        body (UpdateUserProfilePictureBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | UpdateProfilePicture
    """

    return (
        await asyncio_detailed(
            user_id_or_me=user_id_or_me,
            client=client,
            body=body,
        )
    ).parsed
