from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_type import ActivityType
from ..models.item_status import ItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardAnalyticsRecentActivityItem")


@_attrs_define
class DashboardAnalyticsRecentActivityItem:
    """
    Attributes:
        item_id (str | Unset): Item ID
        project_id (str | Unset): Project ID
        project_name (str | Unset): Project name Example: My Project.
        title (str | Unset): Item title Example: New Blog Post.
        status (ItemStatus | Unset): Status of an item in the approval workflow Example: pending.
        timestamp (datetime.datetime | Unset): Activity timestamp Example: 2024-01-15T10:30:00Z.
        activity_type (ActivityType | Unset): Type of activity performed on an item Example: created.
        actor (str | Unset): User who performed the action Example: user@example.com.
        comment (str | Unset): Optional comment Example: Looks good.
    """

    item_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project_name: str | Unset = UNSET
    title: str | Unset = UNSET
    status: ItemStatus | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    activity_type: ActivityType | Unset = UNSET
    actor: str | Unset = UNSET
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        project_id = self.project_id

        project_name = self.project_name

        title = self.title

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        activity_type: str | Unset = UNSET
        if not isinstance(self.activity_type, Unset):
            activity_type = self.activity_type.value

        actor = self.actor

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if actor is not UNSET:
            field_dict["actor"] = actor
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("itemId", UNSET)

        project_id = d.pop("projectId", UNSET)

        project_name = d.pop("projectName", UNSET)

        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: ItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ItemStatus(_status)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        _activity_type = d.pop("activityType", UNSET)
        activity_type: ActivityType | Unset
        if isinstance(_activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = ActivityType(_activity_type)

        actor = d.pop("actor", UNSET)

        comment = d.pop("comment", UNSET)

        dashboard_analytics_recent_activity_item = cls(
            item_id=item_id,
            project_id=project_id,
            project_name=project_name,
            title=title,
            status=status,
            timestamp=timestamp,
            activity_type=activity_type,
            actor=actor,
            comment=comment,
        )

        dashboard_analytics_recent_activity_item.additional_properties = d
        return dashboard_analytics_recent_activity_item

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
