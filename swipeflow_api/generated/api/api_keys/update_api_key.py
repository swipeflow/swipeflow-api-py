from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key import APIKey
from ...models.error_response import ErrorResponse
from ...models.update_api_key_request import UpdateAPIKeyRequest
from ...types import Response


def _get_kwargs(
    key_id: str,
    *,
    body: UpdateAPIKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/api-keys/{key_id}".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIKey | Any | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = APIKey.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIKey | Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAPIKeyRequest,
) -> Response[APIKey | Any | ErrorResponse]:
    """Update API key

     Update an API key's name and/or permissions (partial update).

    Args:
        key_id (str):
        body (UpdateAPIKeyRequest): Partial update — supply only the fields to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKey | Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAPIKeyRequest,
) -> APIKey | Any | ErrorResponse | None:
    """Update API key

     Update an API key's name and/or permissions (partial update).

    Args:
        key_id (str):
        body (UpdateAPIKeyRequest): Partial update — supply only the fields to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKey | Any | ErrorResponse
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAPIKeyRequest,
) -> Response[APIKey | Any | ErrorResponse]:
    """Update API key

     Update an API key's name and/or permissions (partial update).

    Args:
        key_id (str):
        body (UpdateAPIKeyRequest): Partial update — supply only the fields to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIKey | Any | ErrorResponse]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAPIKeyRequest,
) -> APIKey | Any | ErrorResponse | None:
    """Update API key

     Update an API key's name and/or permissions (partial update).

    Args:
        key_id (str):
        body (UpdateAPIKeyRequest): Partial update — supply only the fields to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIKey | Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
            body=body,
        )
    ).parsed
