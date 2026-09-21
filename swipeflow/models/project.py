from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_media_usage import ProjectMediaUsage
    from ..models.project_member import ProjectMember
    from ..models.project_trigger import ProjectTrigger


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        id (str | Unset): Project ID Example: 507f1f77bcf86cd799439011.
        name (str | Unset): Project name Example: My Project.
        description (str | Unset): Project description Example: A sample project for content approval.
        members (list[ProjectMember] | Unset):
        is_archived (bool | Unset): Whether the project is archived Example: False.
        is_starred (bool | Unset): Whether the project is starred Example: True.
        total_items (int | Unset): Total number of items in the project Example: 42.
        pending_items (int | Unset): Number of pending items Example: 5.
        approved_items (int | Unset): Number of approved items Example: 30.
        last_item_posted_at (datetime.datetime | Unset): Timestamp of last item posted Example: 2024-01-15T10:30:00Z.
        triggers (list[ProjectTrigger] | Unset):
        created_at (datetime.datetime | Unset): Project creation timestamp Example: 2024-01-01T00:00:00Z.
        updated_at (datetime.datetime | Unset): Project last update timestamp Example: 2024-01-15T10:30:00Z.
        media_usage (ProjectMediaUsage | Unset): Only present on the single-project detail read (not the list).
            usedBytes counts this project's pending, uploaded, and in-flight-import media — informational; the full quota +
            limit breakdown is at GET /v1/projects/{projectId}/media/usage.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    members: list[ProjectMember] | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    total_items: int | Unset = UNSET
    pending_items: int | Unset = UNSET
    approved_items: int | Unset = UNSET
    last_item_posted_at: datetime.datetime | Unset = UNSET
    triggers: list[ProjectTrigger] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    media_usage: ProjectMediaUsage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        is_archived = self.is_archived

        is_starred = self.is_starred

        total_items = self.total_items

        pending_items = self.pending_items

        approved_items = self.approved_items

        last_item_posted_at: str | Unset = UNSET
        if not isinstance(self.last_item_posted_at, Unset):
            last_item_posted_at = self.last_item_posted_at.isoformat()

        triggers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = []
            for triggers_item_data in self.triggers:
                triggers_item = triggers_item_data.to_dict()
                triggers.append(triggers_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        media_usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media_usage, Unset):
            media_usage = self.media_usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if members is not UNSET:
            field_dict["members"] = members
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_starred is not UNSET:
            field_dict["isStarred"] = is_starred
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if pending_items is not UNSET:
            field_dict["pendingItems"] = pending_items
        if approved_items is not UNSET:
            field_dict["approvedItems"] = approved_items
        if last_item_posted_at is not UNSET:
            field_dict["lastItemPostedAt"] = last_item_posted_at
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if media_usage is not UNSET:
            field_dict["mediaUsage"] = media_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_media_usage import ProjectMediaUsage  # noqa: PLC0415
        from ..models.project_member import ProjectMember  # noqa: PLC0415
        from ..models.project_trigger import ProjectTrigger  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _members = d.pop("members", UNSET)
        members: list[ProjectMember] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = ProjectMember.from_dict(members_item_data)

                members.append(members_item)

        is_archived = d.pop("isArchived", UNSET)

        is_starred = d.pop("isStarred", UNSET)

        total_items = d.pop("totalItems", UNSET)

        pending_items = d.pop("pendingItems", UNSET)

        approved_items = d.pop("approvedItems", UNSET)

        _last_item_posted_at = d.pop("lastItemPostedAt", UNSET)
        last_item_posted_at: datetime.datetime | Unset
        if isinstance(_last_item_posted_at, Unset):
            last_item_posted_at = UNSET
        else:
            last_item_posted_at = datetime.datetime.fromisoformat(_last_item_posted_at)

        _triggers = d.pop("triggers", UNSET)
        triggers: list[ProjectTrigger] | Unset = UNSET
        if _triggers is not UNSET:
            triggers = []
            for triggers_item_data in _triggers:
                triggers_item = ProjectTrigger.from_dict(triggers_item_data)

                triggers.append(triggers_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _media_usage = d.pop("mediaUsage", UNSET)
        media_usage: ProjectMediaUsage | Unset
        if isinstance(_media_usage, Unset):
            media_usage = UNSET
        else:
            media_usage = ProjectMediaUsage.from_dict(_media_usage)

        project = cls(
            id=id,
            name=name,
            description=description,
            members=members,
            is_archived=is_archived,
            is_starred=is_starred,
            total_items=total_items,
            pending_items=pending_items,
            approved_items=approved_items,
            last_item_posted_at=last_item_posted_at,
            triggers=triggers,
            created_at=created_at,
            updated_at=updated_at,
            media_usage=media_usage,
        )

        project.additional_properties = d
        return project

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
