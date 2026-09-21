from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.project import Project
from ...models.update_project_member_request import UpdateProjectMemberRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    member_id: str,
    *,
    body: UpdateProjectMemberRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/members/{member_id}".format(
            project_id=quote(str(project_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
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

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProjectMemberRequest,
) -> Response[ErrorResponse | Project]:
    """Update project member

     Update a member's role in the project

    Args:
        project_id (str):
        member_id (str):
        body (UpdateProjectMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        member_id=member_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProjectMemberRequest,
) -> ErrorResponse | Project | None:
    """Update project member

     Update a member's role in the project

    Args:
        project_id (str):
        member_id (str):
        body (UpdateProjectMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Project
    """

    return sync_detailed(
        project_id=project_id,
        member_id=member_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProjectMemberRequest,
) -> Response[ErrorResponse | Project]:
    """Update project member

     Update a member's role in the project

    Args:
        project_id (str):
        member_id (str):
        body (UpdateProjectMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        member_id=member_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProjectMemberRequest,
) -> ErrorResponse | Project | None:
    """Update project member

     Update a member's role in the project

    Args:
        project_id (str):
        member_id (str):
        body (UpdateProjectMemberRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | Project
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            member_id=member_id,
            client=client,
            body=body,
        )
    ).parsed
