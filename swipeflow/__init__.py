"""SwipeFlow Python SDK.

Endpoints live in ``swipeflow.api.<tag>.<operation_id>`` and models in ``swipeflow.models``;
``SwipeFlowClient`` adds authentication and error handling on top of them.

Example:
    >>> from swipeflow import SwipeFlowClient
    >>> from swipeflow.api.projects.list_projects import sync as list_projects
    >>> with SwipeFlowClient(api_key="your-api-key") as client:
    ...     projects = list_projects(client=client)
"""

from importlib.metadata import PackageNotFoundError, version

from ._wrapper import DEFAULT_BASE_URL, SwipeFlowClient, SwipeFlowError
from .client import AuthenticatedClient, Client

try:
    __version__ = version("swipeflow")
except PackageNotFoundError:
    __version__ = "0+unknown"

__all__ = (
    "AuthenticatedClient",
    "Client",
    "DEFAULT_BASE_URL",
    "SwipeFlowClient",
    "SwipeFlowError",
    "__version__",
)
