"""Thin wrapper over the generated client: API-key auth, defaults, and raising on HTTP errors.

All endpoints and models live in ``swipeflow_api.generated`` and are produced from the
OpenAPI spec by ``scripts/generate.py``; nothing endpoint-specific belongs in this file.
"""

import os
from typing import Any

import httpx

from .generated.client import AuthenticatedClient

DEFAULT_BASE_URL = "https://api.swipeflow.io"
DEFAULT_TIMEOUT = 30.0
API_KEY_ENV_VAR = "SWIPEFLOW_API_KEY"


class SwipeFlowError(Exception):
    """Raised for any HTTP error response (status >= 400)."""

    def __init__(self, response: httpx.Response):
        self.response = response
        self.status_code = response.status_code
        try:
            body = response.json()
        except ValueError:
            body = None
        self.body = body
        self.message = (body.get("message") if isinstance(body, dict) else None) or response.reason_phrase
        self.errors: list[dict[str, Any]] = (body.get("errors") if isinstance(body, dict) else None) or []
        super().__init__(f"{self.status_code} {self.message}")


def _raise_for_status(response: httpx.Response) -> None:
    if response.is_error:
        response.read()
        raise SwipeFlowError(response)


async def _araise_for_status(response: httpx.Response) -> None:
    if response.is_error:
        await response.aread()
        raise SwipeFlowError(response)


class SwipeFlowClient(AuthenticatedClient):
    """Generated ``AuthenticatedClient`` configured for SwipeFlow.

    Authenticates with an API key (``X-API-Key``) taken from ``api_key`` or the
    ``SWIPEFLOW_API_KEY`` environment variable, or with a JWT/OAuth access token
    (``Authorization: Bearer``) passed as ``token``. HTTP errors raise ``SwipeFlowError``.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        **kwargs: Any,
    ):
        if token is None:
            api_key = api_key or os.environ.get(API_KEY_ENV_VAR)
            if not api_key:
                raise ValueError(f"Pass api_key=... (or token=...), or set the {API_KEY_ENV_VAR} environment variable")
            token = api_key
            kwargs.setdefault("prefix", "")
            kwargs.setdefault("auth_header_name", "X-API-Key")
        kwargs.setdefault("timeout", httpx.Timeout(DEFAULT_TIMEOUT))
        super().__init__(base_url=base_url, token=token, **kwargs)

    def get_httpx_client(self) -> httpx.Client:
        created = self._client is None
        client = super().get_httpx_client()
        if created:
            client.event_hooks["response"].append(_raise_for_status)
        return client

    def get_async_httpx_client(self) -> httpx.AsyncClient:
        created = self._async_client is None
        client = super().get_async_httpx_client()
        if created:
            client.event_hooks["response"].append(_araise_for_status)
        return client
