# SwipeFlow Python SDK

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-ISC-green.svg)

Python client for the [SwipeFlow](https://swipeflow.io) API: add manual approval steps to your automation workflows.

Every endpoint and model is **generated from the public OpenAPI spec** (<https://api.swipeflow.io/v1/openapi.json>) with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). The only hand-written code is a small wrapper (`swipeflow/client.py`) that sets the API key, base URL and timeout, and raises on HTTP errors.

## Installation

```bash
pip install swipeflow
```

Requires Python 3.11+.

## Quick start

```python
from swipeflow import SwipeFlowClient
from swipeflow.api.items.create_item import sync as create_item
from swipeflow.api.items.update_item_decision import sync as update_item_decision
from swipeflow.api.projects.list_projects import sync as list_projects
from swipeflow.models import (
    ContentType,
    CreateItemRequest,
    ItemContent,
    UpdateItemDecisionRequest,
    UpdateItemDecisionRequestDecision,
)

with SwipeFlowClient(api_key="your-api-key") as client:
    projects = list_projects(client=client)
    project_id = projects.projects[0].id

    item = create_item(
        project_id=project_id,
        client=client,
        body=CreateItemRequest(
            title="Approve new user signup",
            content=ItemContent(type_=ContentType.TEXT, data="New user John Doe signed up"),
        ),
    )

    update_item_decision(
        project_id=project_id,
        item_id=item.id,
        client=client,
        body=UpdateItemDecisionRequest(
            decision=UpdateItemDecisionRequestDecision.APPROVED,
            comment="User verified",
        ),
    )
```

Instead of passing `api_key`, you can set the `SWIPEFLOW_API_KEY` environment variable and call `SwipeFlowClient()`.

## Using the generated API

Endpoints are modules grouped by API tag under `swipeflow.api`, named after the spec's `operationId` (`swipeflow.api.projects.list_projects`, `swipeflow.api.items.create_item`, ...). Request and response types are in `swipeflow.models`. Each endpoint module exposes four functions:

| Function | Returns |
| --- | --- |
| `sync(...)` | the parsed model |
| `sync_detailed(...)` | `Response` with `status_code`, `headers`, raw `content` and `parsed` |
| `asyncio(...)` | awaitable version of `sync` |
| `asyncio_detailed(...)` | awaitable version of `sync_detailed` |

The examples above import the function you want under the endpoint's name, so calls read like `list_projects(client=client)`:

```python
from swipeflow.api.projects.list_projects import sync as list_projects              # blocking
from swipeflow.api.projects.list_projects import asyncio as list_projects_async     # awaitable
```

Importing the module works too (`from swipeflow.api.projects import list_projects`, then `list_projects.sync(client=client)`), which is handy if you use several variants of the same endpoint.

Endpoints whose spec entry declares no response schema (currently `billing` and a few deletes and redirects) only have the `*_detailed` variants; read the body from `response.content`.

Browse `swipeflow/api/` (or the [OpenAPI spec](https://api.swipeflow.io/v1/openapi.json)) to discover endpoints. Editors autocomplete every parameter and model field.

### Async

```python
import asyncio

from swipeflow import SwipeFlowClient
from swipeflow.api.projects.list_projects import asyncio as list_projects


async def main():
    async with SwipeFlowClient() as client:
        projects = await list_projects(client=client)


asyncio.run(main())
```

## Authentication

| Credential | How |
| --- | --- |
| API key | `SwipeFlowClient(api_key=...)` or `SWIPEFLOW_API_KEY`; sent as `X-API-Key` |
| JWT / OAuth access token | `SwipeFlowClient(token=...)`; sent as `Authorization: Bearer` |

Some account-level endpoints (for example API key management) require an interactive session token and reject API keys with `403`.

## Error handling

HTTP errors (status >= 400) raise `SwipeFlowError`:

```python
from swipeflow import SwipeFlowError
from swipeflow.api.projects.get_project import sync as get_project

try:
    get_project(project_id="000000000000000000000000", client=client)
except SwipeFlowError as e:
    print(e.status_code)  # 404
    print(e.message)      # "Project not found"
    print(e.errors)       # field-level validation errors, if any
    print(e.response)     # the underlying httpx.Response
```

Network failures and timeouts raise the usual `httpx` exceptions.

## Configuration

`SwipeFlowClient` accepts every argument of the generated `AuthenticatedClient`, for example:

```python
import httpx

client = SwipeFlowClient(
    api_key="your-api-key",
    base_url="https://staging-api.swipeflow.io",  # default: https://api.swipeflow.io
    timeout=httpx.Timeout(60.0),                   # default: 30s
    headers={"X-Custom": "1"},
)
```

## Development

```bash
git clone https://github.com/swipeflow/swipeflow-sdk-py.git
cd swipeflow-sdk-py
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Set `SWIPEFLOW_API_KEY` to also run the read-only live tests in `tests/test_live.py`.

### Regenerating from the spec

```bash
python scripts/generate.py                  # download the live spec and regenerate
python scripts/generate.py --spec ./my.json # or generate from another spec (URL or file)
```

This replaces the generated files in `swipeflow/` (`api/`, `models/`, `client.py`, `errors.py`, `types.py` and `__init__.py`, the last one from `templates/package_init.py.jinja`). **Never edit those by hand**; change the OpenAPI spec (or the generator flags and template in `scripts/`) instead. The generated code is committed so that installing from git works without a generation step; regenerate and commit it whenever the API changes.

Method names come from each operation's `operationId` in the spec; operations without one get names derived from their path.

### Project layout

```
swipeflow/
├── _wrapper.py     # hand-written: SwipeFlowClient + SwipeFlowError
├── py.typed
├── __init__.py     # generated from templates/package_init.py.jinja
├── api/            # generated: api/<tag>/<operation>.py
├── models/         # generated
└── client.py, errors.py, types.py  # generated
templates/package_init.py.jinja
scripts/generate.py # download spec + run the generator
tests/
```

## License

ISC
