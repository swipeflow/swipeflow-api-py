import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_event_page import AuditEventPage
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    subject: str | Unset = UNSET,
    item_id: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["type"] = type_

    params["actor"] = actor

    params["subject"] = subject

    params["itemId"] = item_id

    params["targetId"] = target_id

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/audit-events".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditEventPage | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AuditEventPage.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditEventPage | ErrorResponse]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    subject: str | Unset = UNSET,
    item_id: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[AuditEventPage | ErrorResponse]:
    """List project audit events

     Paginated, newest-first activity feed for the project (epic #276). A platform admin
    or a project OWNER/ADMIN sees every event. A regular member sees all non-sensitive
    events plus any sensitive event (membership, webhook, API-key changes) they
    performed or are the subject of.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        actor (str | Unset):
        subject (str | Unset):
        item_id (str | Unset):
        target_id (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cursor=cursor,
        limit=limit,
        type_=type_,
        actor=actor,
        subject=subject,
        item_id=item_id,
        target_id=target_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    subject: str | Unset = UNSET,
    item_id: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> AuditEventPage | ErrorResponse | None:
    """List project audit events

     Paginated, newest-first activity feed for the project (epic #276). A platform admin
    or a project OWNER/ADMIN sees every event. A regular member sees all non-sensitive
    events plus any sensitive event (membership, webhook, API-key changes) they
    performed or are the subject of.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        actor (str | Unset):
        subject (str | Unset):
        item_id (str | Unset):
        target_id (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventPage | ErrorResponse
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        cursor=cursor,
        limit=limit,
        type_=type_,
        actor=actor,
        subject=subject,
        item_id=item_id,
        target_id=target_id,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    subject: str | Unset = UNSET,
    item_id: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[AuditEventPage | ErrorResponse]:
    """List project audit events

     Paginated, newest-first activity feed for the project (epic #276). A platform admin
    or a project OWNER/ADMIN sees every event. A regular member sees all non-sensitive
    events plus any sensitive event (membership, webhook, API-key changes) they
    performed or are the subject of.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        actor (str | Unset):
        subject (str | Unset):
        item_id (str | Unset):
        target_id (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventPage | ErrorResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cursor=cursor,
        limit=limit,
        type_=type_,
        actor=actor,
        subject=subject,
        item_id=item_id,
        target_id=target_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    type_: str | Unset = UNSET,
    actor: str | Unset = UNSET,
    subject: str | Unset = UNSET,
    item_id: str | Unset = UNSET,
    target_id: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> AuditEventPage | ErrorResponse | None:
    """List project audit events

     Paginated, newest-first activity feed for the project (epic #276). A platform admin
    or a project OWNER/ADMIN sees every event. A regular member sees all non-sensitive
    events plus any sensitive event (membership, webhook, API-key changes) they
    performed or are the subject of.

    Args:
        project_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        type_ (str | Unset):
        actor (str | Unset):
        subject (str | Unset):
        item_id (str | Unset):
        target_id (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventPage | ErrorResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            cursor=cursor,
            limit=limit,
            type_=type_,
            actor=actor,
            subject=subject,
            item_id=item_id,
            target_id=target_id,
            from_=from_,
            to=to,
        )
    ).parsed
