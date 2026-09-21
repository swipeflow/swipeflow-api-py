"""SwipeFlow Python SDK.

The API surface (``swipeflow_api.generated``) is generated from the public OpenAPI spec;
``SwipeFlowClient`` only adds authentication and error handling on top of it.

Example:
    >>> from swipeflow_api import SwipeFlowClient
    >>> from swipeflow_api.generated.api.projects import list_projects
    >>> with SwipeFlowClient(api_key="your-api-key") as client:
    ...     projects = list_projects.sync(client=client)
"""

from importlib.metadata import PackageNotFoundError, version

from .client import DEFAULT_BASE_URL, SwipeFlowClient, SwipeFlowError

try:
    __version__ = version("swipeflow-api")
except PackageNotFoundError:
    __version__ = "0+unknown"

__all__ = ["DEFAULT_BASE_URL", "SwipeFlowClient", "SwipeFlowError", "__version__"]
