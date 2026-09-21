from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_media_upload_body import CreateMediaUploadBody
from ...models.create_media_upload_response_201 import CreateMediaUploadResponse201
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateMediaUploadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/media-uploads".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateMediaUploadResponse201 | None:
    if response.status_code == 201:
        response_201 = CreateMediaUploadResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateMediaUploadResponse201]:
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
    body: CreateMediaUploadBody,
) -> Response[Any | CreateMediaUploadResponse201]:
    """Request a media upload ticket

     Media is uploaded directly to storage, not through this API, in two steps. Step 1 (this call): send
    the filename, exact byte size, and MIME type; the response contains a presigned, exact-size, write-
    once `PUT` target (`upload.url` + `upload.headers`) that the client sends the raw bytes to with
    those exact headers, e.g. `curl -X PUT "$url" $(for k in ...; do echo -H "$k: ..."; done) --data-
    binary @path`. Step 2: `POST /v1/media-uploads/{id}/confirm` once the upload completes. From there,
    using the media is ordinary item usage, not a further upload step: attach it to an item and/or embed
    its `ref` inside the item's markdown/HTML content — refs are swapped for short-lived signed URLs
    when the item is read. The declared `fileSize` is reserved against the account's media quota
    immediately; an unconfirmed ticket is reclaimed after it expires.

    Args:
        project_id (str):
        body (CreateMediaUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateMediaUploadResponse201]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMediaUploadBody,
) -> Any | CreateMediaUploadResponse201 | None:
    """Request a media upload ticket

     Media is uploaded directly to storage, not through this API, in two steps. Step 1 (this call): send
    the filename, exact byte size, and MIME type; the response contains a presigned, exact-size, write-
    once `PUT` target (`upload.url` + `upload.headers`) that the client sends the raw bytes to with
    those exact headers, e.g. `curl -X PUT "$url" $(for k in ...; do echo -H "$k: ..."; done) --data-
    binary @path`. Step 2: `POST /v1/media-uploads/{id}/confirm` once the upload completes. From there,
    using the media is ordinary item usage, not a further upload step: attach it to an item and/or embed
    its `ref` inside the item's markdown/HTML content — refs are swapped for short-lived signed URLs
    when the item is read. The declared `fileSize` is reserved against the account's media quota
    immediately; an unconfirmed ticket is reclaimed after it expires.

    Args:
        project_id (str):
        body (CreateMediaUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateMediaUploadResponse201
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMediaUploadBody,
) -> Response[Any | CreateMediaUploadResponse201]:
    """Request a media upload ticket

     Media is uploaded directly to storage, not through this API, in two steps. Step 1 (this call): send
    the filename, exact byte size, and MIME type; the response contains a presigned, exact-size, write-
    once `PUT` target (`upload.url` + `upload.headers`) that the client sends the raw bytes to with
    those exact headers, e.g. `curl -X PUT "$url" $(for k in ...; do echo -H "$k: ..."; done) --data-
    binary @path`. Step 2: `POST /v1/media-uploads/{id}/confirm` once the upload completes. From there,
    using the media is ordinary item usage, not a further upload step: attach it to an item and/or embed
    its `ref` inside the item's markdown/HTML content — refs are swapped for short-lived signed URLs
    when the item is read. The declared `fileSize` is reserved against the account's media quota
    immediately; an unconfirmed ticket is reclaimed after it expires.

    Args:
        project_id (str):
        body (CreateMediaUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateMediaUploadResponse201]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMediaUploadBody,
) -> Any | CreateMediaUploadResponse201 | None:
    """Request a media upload ticket

     Media is uploaded directly to storage, not through this API, in two steps. Step 1 (this call): send
    the filename, exact byte size, and MIME type; the response contains a presigned, exact-size, write-
    once `PUT` target (`upload.url` + `upload.headers`) that the client sends the raw bytes to with
    those exact headers, e.g. `curl -X PUT "$url" $(for k in ...; do echo -H "$k: ..."; done) --data-
    binary @path`. Step 2: `POST /v1/media-uploads/{id}/confirm` once the upload completes. From there,
    using the media is ordinary item usage, not a further upload step: attach it to an item and/or embed
    its `ref` inside the item's markdown/HTML content — refs are swapped for short-lived signed URLs
    when the item is read. The declared `fileSize` is reserved against the account's media quota
    immediately; an unconfirmed ticket is reclaimed after it expires.

    Args:
        project_id (str):
        body (CreateMediaUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateMediaUploadResponse201
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
