from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_analytics_project_status_item import (
        DashboardAnalyticsProjectStatusItem,
    )
    from ..models.dashboard_analytics_recent_activity_item import (
        DashboardAnalyticsRecentActivityItem,
    )
    from ..models.dashboard_analytics_trends import DashboardAnalyticsTrends


T = TypeVar("T", bound="DashboardAnalytics")


@_attrs_define
class DashboardAnalytics:
    """
    Attributes:
        pending_approvals (int | Unset): Number of pending approvals Example: 25.
        trends (DashboardAnalyticsTrends | Unset): Trend data for various metrics
        average_response_time (float | Unset): Average response time in hours Example: 24.5.
        approval_rate (int | Unset): Approval rate percentage Example: 85.
        completion_rate (int | Unset): Completion rate percentage Example: 75.
        daily_new_items (int | Unset): Number of new items created today Example: 5.
        recent_activity (list[DashboardAnalyticsRecentActivityItem] | Unset):
        project_status (list[DashboardAnalyticsProjectStatusItem] | Unset):
    """

    pending_approvals: int | Unset = UNSET
    trends: DashboardAnalyticsTrends | Unset = UNSET
    average_response_time: float | Unset = UNSET
    approval_rate: int | Unset = UNSET
    completion_rate: int | Unset = UNSET
    daily_new_items: int | Unset = UNSET
    recent_activity: list[DashboardAnalyticsRecentActivityItem] | Unset = UNSET
    project_status: list[DashboardAnalyticsProjectStatusItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_approvals = self.pending_approvals

        trends: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trends, Unset):
            trends = self.trends.to_dict()

        average_response_time = self.average_response_time

        approval_rate = self.approval_rate

        completion_rate = self.completion_rate

        daily_new_items = self.daily_new_items

        recent_activity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_activity, Unset):
            recent_activity = []
            for recent_activity_item_data in self.recent_activity:
                recent_activity_item = recent_activity_item_data.to_dict()
                recent_activity.append(recent_activity_item)

        project_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.project_status, Unset):
            project_status = []
            for project_status_item_data in self.project_status:
                project_status_item = project_status_item_data.to_dict()
                project_status.append(project_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_approvals is not UNSET:
            field_dict["pendingApprovals"] = pending_approvals
        if trends is not UNSET:
            field_dict["trends"] = trends
        if average_response_time is not UNSET:
            field_dict["averageResponseTime"] = average_response_time
        if approval_rate is not UNSET:
            field_dict["approvalRate"] = approval_rate
        if completion_rate is not UNSET:
            field_dict["completionRate"] = completion_rate
        if daily_new_items is not UNSET:
            field_dict["dailyNewItems"] = daily_new_items
        if recent_activity is not UNSET:
            field_dict["recentActivity"] = recent_activity
        if project_status is not UNSET:
            field_dict["projectStatus"] = project_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_analytics_project_status_item import (
            DashboardAnalyticsProjectStatusItem,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_recent_activity_item import (
            DashboardAnalyticsRecentActivityItem,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_trends import (
            DashboardAnalyticsTrends,  # noqa: PLC0415
        )

        d = dict(src_dict)
        pending_approvals = d.pop("pendingApprovals", UNSET)

        _trends = d.pop("trends", UNSET)
        trends: DashboardAnalyticsTrends | Unset
        if isinstance(_trends, Unset):
            trends = UNSET
        else:
            trends = DashboardAnalyticsTrends.from_dict(_trends)

        average_response_time = d.pop("averageResponseTime", UNSET)

        approval_rate = d.pop("approvalRate", UNSET)

        completion_rate = d.pop("completionRate", UNSET)

        daily_new_items = d.pop("dailyNewItems", UNSET)

        _recent_activity = d.pop("recentActivity", UNSET)
        recent_activity: list[DashboardAnalyticsRecentActivityItem] | Unset = UNSET
        if _recent_activity is not UNSET:
            recent_activity = []
            for recent_activity_item_data in _recent_activity:
                recent_activity_item = DashboardAnalyticsRecentActivityItem.from_dict(
                    recent_activity_item_data
                )

                recent_activity.append(recent_activity_item)

        _project_status = d.pop("projectStatus", UNSET)
        project_status: list[DashboardAnalyticsProjectStatusItem] | Unset = UNSET
        if _project_status is not UNSET:
            project_status = []
            for project_status_item_data in _project_status:
                project_status_item = DashboardAnalyticsProjectStatusItem.from_dict(
                    project_status_item_data
                )

                project_status.append(project_status_item)

        dashboard_analytics = cls(
            pending_approvals=pending_approvals,
            trends=trends,
            average_response_time=average_response_time,
            approval_rate=approval_rate,
            completion_rate=completion_rate,
            daily_new_items=daily_new_items,
            recent_activity=recent_activity,
            project_status=project_status,
        )

        dashboard_analytics.additional_properties = d
        return dashboard_analytics

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
