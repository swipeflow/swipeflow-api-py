from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_version_status import ItemVersionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_media import AttachedMedia
    from ..models.item_content import ItemContent
    from ..models.item_decision import ItemDecision
    from ..models.item_version_metadata import ItemVersionMetadata


T = TypeVar("T", bound="ItemVersion")


@_attrs_define
class ItemVersion:
    """
    Attributes:
        id (str | Unset): Version ID Example: 507f1f77bcf86cd799439011.
        item_id (str | Unset): Item ID Example: 507f1f77bcf86cd799439012.
        project_id (str | Unset): Project ID Example: 507f1f77bcf86cd799439013.
        version (int | Unset): Version number Example: 2.
        title (str | Unset): Item title at this version Example: Updated Title.
        description (str | Unset): Item description at this version Example: Updated description.
        content (ItemContent | Unset):
        media (list[AttachedMedia] | Unset): This version's own frozen snapshot of attached media — not affected by
            later versions' attachments.
        metadata (ItemVersionMetadata | Unset): Custom metadata at this version Example: {'author': 'John Doe'}.
        status (ItemVersionStatus | Unset): Status at this version Example: pending.
        decisions (list[ItemDecision] | Unset):
        created_by (str | Unset): User who created this version Example: 507f1f77bcf86cd799439014.
        actor_name (str | Unset): Display name of who submitted this version (user, API key, or OAuth client name)
            Example: Claude.
        created_at (datetime.datetime | Unset): When this version was created / submitted (v1 == item creation) Example:
            2024-01-15T10:30:00Z.
    """

    id: str | Unset = UNSET
    item_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    version: int | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    content: ItemContent | Unset = UNSET
    media: list[AttachedMedia] | Unset = UNSET
    metadata: ItemVersionMetadata | Unset = UNSET
    status: ItemVersionStatus | Unset = UNSET
    decisions: list[ItemDecision] | Unset = UNSET
    created_by: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_id = self.item_id

        project_id = self.project_id

        version = self.version

        title = self.title

        description = self.description

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        media: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = []
            for media_item_data in self.media:
                media_item = media_item_data.to_dict()
                media.append(media_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        decisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.decisions, Unset):
            decisions = []
            for decisions_item_data in self.decisions:
                decisions_item = decisions_item_data.to_dict()
                decisions.append(decisions_item)

        created_by = self.created_by

        actor_name = self.actor_name

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if version is not UNSET:
            field_dict["version"] = version
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if content is not UNSET:
            field_dict["content"] = content
        if media is not UNSET:
            field_dict["media"] = media
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if decisions is not UNSET:
            field_dict["decisions"] = decisions
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_media import AttachedMedia  # noqa: PLC0415
        from ..models.item_content import ItemContent  # noqa: PLC0415
        from ..models.item_decision import ItemDecision  # noqa: PLC0415
        from ..models.item_version_metadata import ItemVersionMetadata  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        item_id = d.pop("itemId", UNSET)

        project_id = d.pop("projectId", UNSET)

        version = d.pop("version", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _content = d.pop("content", UNSET)
        content: ItemContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ItemContent.from_dict(_content)

        _media = d.pop("media", UNSET)
        media: list[AttachedMedia] | Unset = UNSET
        if _media is not UNSET:
            media = []
            for media_item_data in _media:
                media_item = AttachedMedia.from_dict(media_item_data)

                media.append(media_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: ItemVersionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ItemVersionMetadata.from_dict(_metadata)

        _status = d.pop("status", UNSET)
        status: ItemVersionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ItemVersionStatus(_status)

        _decisions = d.pop("decisions", UNSET)
        decisions: list[ItemDecision] | Unset = UNSET
        if _decisions is not UNSET:
            decisions = []
            for decisions_item_data in _decisions:
                decisions_item = ItemDecision.from_dict(decisions_item_data)

                decisions.append(decisions_item)

        created_by = d.pop("createdBy", UNSET)

        actor_name = d.pop("actorName", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        item_version = cls(
            id=id,
            item_id=item_id,
            project_id=project_id,
            version=version,
            title=title,
            description=description,
            content=content,
            media=media,
            metadata=metadata,
            status=status,
            decisions=decisions,
            created_by=created_by,
            actor_name=actor_name,
            created_at=created_at,
        )

        item_version.additional_properties = d
        return item_version

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
