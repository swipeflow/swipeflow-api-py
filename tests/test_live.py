"""Read-only smoke test against the real API; skipped unless SWIPEFLOW_API_KEY is set."""

import os

import pytest

from swipeflow_api import SwipeFlowClient, SwipeFlowError
from swipeflow_api.generated.api.projects import get_project, list_projects
from swipeflow_api.generated.models import ProjectList

pytestmark = pytest.mark.skipif(not os.environ.get("SWIPEFLOW_API_KEY"), reason="SWIPEFLOW_API_KEY not set")


def test_list_projects_parses_real_response():
    with SwipeFlowClient() as client:
        assert isinstance(list_projects.sync(client=client), ProjectList)


def test_missing_project_raises():
    with SwipeFlowClient() as client:
        with pytest.raises(SwipeFlowError) as excinfo:
            get_project.sync(project_id="000000000000000000000000", client=client)
    assert excinfo.value.status_code == 404
