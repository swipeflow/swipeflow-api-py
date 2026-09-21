from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_analytics_trends_approval_rate import (
        DashboardAnalyticsTrendsApprovalRate,
    )
    from ..models.dashboard_analytics_trends_completion_rate import (
        DashboardAnalyticsTrendsCompletionRate,
    )
    from ..models.dashboard_analytics_trends_daily_new_items import (
        DashboardAnalyticsTrendsDailyNewItems,
    )
    from ..models.dashboard_analytics_trends_pending_approvals import (
        DashboardAnalyticsTrendsPendingApprovals,
    )
    from ..models.dashboard_analytics_trends_response_time import (
        DashboardAnalyticsTrendsResponseTime,
    )


T = TypeVar("T", bound="DashboardAnalyticsTrends")


@_attrs_define
class DashboardAnalyticsTrends:
    """Trend data for various metrics

    Attributes:
        pending_approvals (DashboardAnalyticsTrendsPendingApprovals | Unset):
        approval_rate (DashboardAnalyticsTrendsApprovalRate | Unset):
        completion_rate (DashboardAnalyticsTrendsCompletionRate | Unset):
        response_time (DashboardAnalyticsTrendsResponseTime | Unset):
        daily_new_items (DashboardAnalyticsTrendsDailyNewItems | Unset):
    """

    pending_approvals: DashboardAnalyticsTrendsPendingApprovals | Unset = UNSET
    approval_rate: DashboardAnalyticsTrendsApprovalRate | Unset = UNSET
    completion_rate: DashboardAnalyticsTrendsCompletionRate | Unset = UNSET
    response_time: DashboardAnalyticsTrendsResponseTime | Unset = UNSET
    daily_new_items: DashboardAnalyticsTrendsDailyNewItems | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_approvals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pending_approvals, Unset):
            pending_approvals = self.pending_approvals.to_dict()

        approval_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.approval_rate, Unset):
            approval_rate = self.approval_rate.to_dict()

        completion_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.completion_rate, Unset):
            completion_rate = self.completion_rate.to_dict()

        response_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_time, Unset):
            response_time = self.response_time.to_dict()

        daily_new_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_new_items, Unset):
            daily_new_items = self.daily_new_items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_approvals is not UNSET:
            field_dict["pendingApprovals"] = pending_approvals
        if approval_rate is not UNSET:
            field_dict["approvalRate"] = approval_rate
        if completion_rate is not UNSET:
            field_dict["completionRate"] = completion_rate
        if response_time is not UNSET:
            field_dict["responseTime"] = response_time
        if daily_new_items is not UNSET:
            field_dict["dailyNewItems"] = daily_new_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_analytics_trends_approval_rate import (
            DashboardAnalyticsTrendsApprovalRate,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_trends_completion_rate import (
            DashboardAnalyticsTrendsCompletionRate,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_trends_daily_new_items import (
            DashboardAnalyticsTrendsDailyNewItems,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_trends_pending_approvals import (
            DashboardAnalyticsTrendsPendingApprovals,  # noqa: PLC0415
        )
        from ..models.dashboard_analytics_trends_response_time import (
            DashboardAnalyticsTrendsResponseTime,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _pending_approvals = d.pop("pendingApprovals", UNSET)
        pending_approvals: DashboardAnalyticsTrendsPendingApprovals | Unset
        if isinstance(_pending_approvals, Unset):
            pending_approvals = UNSET
        else:
            pending_approvals = DashboardAnalyticsTrendsPendingApprovals.from_dict(
                _pending_approvals
            )

        _approval_rate = d.pop("approvalRate", UNSET)
        approval_rate: DashboardAnalyticsTrendsApprovalRate | Unset
        if isinstance(_approval_rate, Unset):
            approval_rate = UNSET
        else:
            approval_rate = DashboardAnalyticsTrendsApprovalRate.from_dict(
                _approval_rate
            )

        _completion_rate = d.pop("completionRate", UNSET)
        completion_rate: DashboardAnalyticsTrendsCompletionRate | Unset
        if isinstance(_completion_rate, Unset):
            completion_rate = UNSET
        else:
            completion_rate = DashboardAnalyticsTrendsCompletionRate.from_dict(
                _completion_rate
            )

        _response_time = d.pop("responseTime", UNSET)
        response_time: DashboardAnalyticsTrendsResponseTime | Unset
        if isinstance(_response_time, Unset):
            response_time = UNSET
        else:
            response_time = DashboardAnalyticsTrendsResponseTime.from_dict(
                _response_time
            )

        _daily_new_items = d.pop("dailyNewItems", UNSET)
        daily_new_items: DashboardAnalyticsTrendsDailyNewItems | Unset
        if isinstance(_daily_new_items, Unset):
            daily_new_items = UNSET
        else:
            daily_new_items = DashboardAnalyticsTrendsDailyNewItems.from_dict(
                _daily_new_items
            )

        dashboard_analytics_trends = cls(
            pending_approvals=pending_approvals,
            approval_rate=approval_rate,
            completion_rate=completion_rate,
            response_time=response_time,
            daily_new_items=daily_new_items,
        )

        dashboard_analytics_trends.additional_properties = d
        return dashboard_analytics_trends

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
