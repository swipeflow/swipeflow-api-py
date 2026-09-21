from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_projects_owner_status import ListProjectsOwnerStatus
from ...models.list_projects_sort import ListProjectsSort
from ...models.list_projects_status import ListProjectsStatus
from ...models.project_list import ProjectList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: str | Unset = UNSET,
    sort: ListProjectsSort | Unset = ListProjectsSort.UPDATEDAT,
    fields: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: ListProjectsStatus | Unset = UNSET,
    starred: bool | Unset = UNSET,
    include_all: bool | Unset = False,
    member_user_id: str | Unset = UNSET,
    owner_user_id: str | Unset = UNSET,
    created_from: str | Unset = UNSET,
    created_to: str | Unset = UNSET,
    owner_status: ListProjectsOwnerStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["fields"] = fields

    params["page"] = page

    params["limit"] = limit

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["starred"] = starred

    params["includeAll"] = include_all

    params["memberUserId"] = member_user_id

    params["ownerUserId"] = owner_user_id

    params["createdFrom"] = created_from

    params["createdTo"] = created_to

    json_owner_status: str | Unset = UNSET
    if not isinstance(owner_status, Unset):
        json_owner_status = owner_status.value

    params["ownerStatus"] = json_owner_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ProjectList | None:
    if response.status_code == 200:
        response_200 = ProjectList.from_dict(response.json())

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
) -> Response[ErrorResponse | ProjectList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    sort: ListProjectsSort | Unset = ListProjectsSort.UPDATEDAT,
    fields: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: ListProjectsStatus | Unset = UNSET,
    starred: bool | Unset = UNSET,
    include_all: bool | Unset = False,
    member_user_id: str | Unset = UNSET,
    owner_user_id: str | Unset = UNSET,
    created_from: str | Unset = UNSET,
    created_to: str | Unset = UNSET,
    owner_status: ListProjectsOwnerStatus | Unset = UNSET,
) -> Response[ErrorResponse | ProjectList]:
    """Get all projects

     Retrieve a list of all projects for the authenticated user with pagination, search, and filtering
    options.

    Args:
        search (str | Unset):
        sort (ListProjectsSort | Unset):  Default: ListProjectsSort.UPDATEDAT.
        fields (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        status (ListProjectsStatus | Unset):
        starred (bool | Unset):
        include_all (bool | Unset):  Default: False.
        member_user_id (str | Unset):
        owner_user_id (str | Unset):
        created_from (str | Unset):
        created_to (str | Unset):
        owner_status (ListProjectsOwnerStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectList]
    """

    kwargs = _get_kwargs(
        search=search,
        sort=sort,
        fields=fields,
        page=page,
        limit=limit,
        status=status,
        starred=starred,
        include_all=include_all,
        member_user_id=member_user_id,
        owner_user_id=owner_user_id,
        created_from=created_from,
        created_to=created_to,
        owner_status=owner_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    sort: ListProjectsSort | Unset = ListProjectsSort.UPDATEDAT,
    fields: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: ListProjectsStatus | Unset = UNSET,
    starred: bool | Unset = UNSET,
    include_all: bool | Unset = False,
    member_user_id: str | Unset = UNSET,
    owner_user_id: str | Unset = UNSET,
    created_from: str | Unset = UNSET,
    created_to: str | Unset = UNSET,
    owner_status: ListProjectsOwnerStatus | Unset = UNSET,
) -> ErrorResponse | ProjectList | None:
    """Get all projects

     Retrieve a list of all projects for the authenticated user with pagination, search, and filtering
    options.

    Args:
        search (str | Unset):
        sort (ListProjectsSort | Unset):  Default: ListProjectsSort.UPDATEDAT.
        fields (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        status (ListProjectsStatus | Unset):
        starred (bool | Unset):
        include_all (bool | Unset):  Default: False.
        member_user_id (str | Unset):
        owner_user_id (str | Unset):
        created_from (str | Unset):
        created_to (str | Unset):
        owner_status (ListProjectsOwnerStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectList
    """

    return sync_detailed(
        client=client,
        search=search,
        sort=sort,
        fields=fields,
        page=page,
        limit=limit,
        status=status,
        starred=starred,
        include_all=include_all,
        member_user_id=member_user_id,
        owner_user_id=owner_user_id,
        created_from=created_from,
        created_to=created_to,
        owner_status=owner_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    sort: ListProjectsSort | Unset = ListProjectsSort.UPDATEDAT,
    fields: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: ListProjectsStatus | Unset = UNSET,
    starred: bool | Unset = UNSET,
    include_all: bool | Unset = False,
    member_user_id: str | Unset = UNSET,
    owner_user_id: str | Unset = UNSET,
    created_from: str | Unset = UNSET,
    created_to: str | Unset = UNSET,
    owner_status: ListProjectsOwnerStatus | Unset = UNSET,
) -> Response[ErrorResponse | ProjectList]:
    """Get all projects

     Retrieve a list of all projects for the authenticated user with pagination, search, and filtering
    options.

    Args:
        search (str | Unset):
        sort (ListProjectsSort | Unset):  Default: ListProjectsSort.UPDATEDAT.
        fields (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        status (ListProjectsStatus | Unset):
        starred (bool | Unset):
        include_all (bool | Unset):  Default: False.
        member_user_id (str | Unset):
        owner_user_id (str | Unset):
        created_from (str | Unset):
        created_to (str | Unset):
        owner_status (ListProjectsOwnerStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ProjectList]
    """

    kwargs = _get_kwargs(
        search=search,
        sort=sort,
        fields=fields,
        page=page,
        limit=limit,
        status=status,
        starred=starred,
        include_all=include_all,
        member_user_id=member_user_id,
        owner_user_id=owner_user_id,
        created_from=created_from,
        created_to=created_to,
        owner_status=owner_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    sort: ListProjectsSort | Unset = ListProjectsSort.UPDATEDAT,
    fields: str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    status: ListProjectsStatus | Unset = UNSET,
    starred: bool | Unset = UNSET,
    include_all: bool | Unset = False,
    member_user_id: str | Unset = UNSET,
    owner_user_id: str | Unset = UNSET,
    created_from: str | Unset = UNSET,
    created_to: str | Unset = UNSET,
    owner_status: ListProjectsOwnerStatus | Unset = UNSET,
) -> ErrorResponse | ProjectList | None:
    """Get all projects

     Retrieve a list of all projects for the authenticated user with pagination, search, and filtering
    options.

    Args:
        search (str | Unset):
        sort (ListProjectsSort | Unset):  Default: ListProjectsSort.UPDATEDAT.
        fields (str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        status (ListProjectsStatus | Unset):
        starred (bool | Unset):
        include_all (bool | Unset):  Default: False.
        member_user_id (str | Unset):
        owner_user_id (str | Unset):
        created_from (str | Unset):
        created_to (str | Unset):
        owner_status (ListProjectsOwnerStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ProjectList
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            sort=sort,
            fields=fields,
            page=page,
            limit=limit,
            status=status,
            starred=starred,
            include_all=include_all,
            member_user_id=member_user_id,
            owner_user_id=owner_user_id,
            created_from=created_from,
            created_to=created_to,
            owner_status=owner_status,
        )
    ).parsed
