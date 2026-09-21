from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecentProject")


@_attrs_define
class RecentProject:
    """
    Attributes:
        project_id (str | Unset): Project ID Example: 507f1f77bcf86cd799439011.
        name (str | Unset): Project name Example: My Project.
        pending_count (float | Unset): Number of pending items Example: 5.
        last_accessed_at (datetime.datetime | Unset): Last access timestamp Example: 2024-01-15T10:30:00Z.
    """

    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    pending_count: float | Unset = UNSET
    last_accessed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        name = self.name

        pending_count = self.pending_count

        last_accessed_at: str | Unset = UNSET
        if not isinstance(self.last_accessed_at, Unset):
            last_accessed_at = self.last_accessed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if pending_count is not UNSET:
            field_dict["pendingCount"] = pending_count
        if last_accessed_at is not UNSET:
            field_dict["lastAccessedAt"] = last_accessed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId", UNSET)

        name = d.pop("name", UNSET)

        pending_count = d.pop("pendingCount", UNSET)

        _last_accessed_at = d.pop("lastAccessedAt", UNSET)
        last_accessed_at: datetime.datetime | Unset
        if isinstance(_last_accessed_at, Unset):
            last_accessed_at = UNSET
        else:
            last_accessed_at = datetime.datetime.fromisoformat(_last_accessed_at)

        recent_project = cls(
            project_id=project_id,
            name=name,
            pending_count=pending_count,
            last_accessed_at=last_accessed_at,
        )

        recent_project.additional_properties = d
        return recent_project

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
