from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_request import CreateProjectRequest
from ...models.error_response import ErrorResponse
from ...models.project import Project
from ...types import Response


def _get_kwargs(
    *,
    body: CreateProjectRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Project.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateProjectRequest,
) -> Response[ErrorResponse | Project]:
    """Resolve or create a project by name

     Looks up a project the caller belongs to with a matching name (case-insensitive) and returns it; if
    none exists, creates one. Lets a caller name a project without first checking whether it exists. Not
    a strict guarantee under concurrent calls with a brand-new name — see resolveOrCreateProject in
    ProjectService.

    Args:
        body (CreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Project]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateProjectRequest,
) -> ErrorResponse | Project | None:
    """Resolve or create a project by name

     Looks up a project the caller belongs to with a matching name (case-insensitive) and returns it; if
    none exists, creates one. Lets a caller name a project without first checking whether it exists. Not
    a strict guarantee under concurrent calls with a brand-new name — see resolveOrCreateProject in
    ProjectService.

    Args:
        body (CreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Project
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateProjectRequest,
) -> Response[ErrorResponse | Project]:
    """Resolve or create a project by name

     Looks up a project the caller belongs to with a matching name (case-insensitive) and returns it; if
    none exists, creates one. Lets a caller name a project without first checking whether it exists. Not
    a strict guarantee under concurrent calls with a brand-new name — see resolveOrCreateProject in
    ProjectService.

    Args:
        body (CreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Project]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateProjectRequest,
) -> ErrorResponse | Project | None:
    """Resolve or create a project by name

     Looks up a project the caller belongs to with a matching name (case-insensitive) and returns it; if
    none exists, creates one. Lets a caller name a project without first checking whether it exists. Not
    a strict guarantee under concurrent calls with a brand-new name — see resolveOrCreateProject in
    ProjectService.

    Args:
        body (CreateProjectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Project
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
