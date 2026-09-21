from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_status import ItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_media import AttachedMedia
    from ..models.item_content import ItemContent
    from ..models.item_decision import ItemDecision
    from ..models.item_metadata import ItemMetadata
    from ..models.item_processed import ItemProcessed
    from ..models.item_version import ItemVersion


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        id (str | Unset): Item ID Example: 507f1f77bcf86cd799439011.
        project_id (str | Unset): Project ID Example: 507f1f77bcf86cd799439012.
        title (str | Unset): Item title Example: New Blog Post.
        description (str | Unset): Item description Example: A blog post about API design.
        content (ItemContent | Unset):
        media (list[AttachedMedia] | Unset): Media currently attached to this item — always a superset of whatever
            `content.data` embeds, plus anything attached without being inline. Reflects the *current* state only, same as
            `content`; an `ItemVersion`'s own `media` is that version's frozen snapshot instead.
        metadata (ItemMetadata | Unset): Custom metadata Example: {'author': 'John Doe', 'category': 'Technology'}.
        status (ItemStatus | Unset): Status of an item in the approval workflow Example: pending.
        decisions (list[ItemDecision] | Unset):
        processed (ItemProcessed | None | Unset): Set once the requester has confirmed it acted on the decision (see PUT
            /:itemId/processed). Only ever present on 'approved'/'rejected' items — null everywhere else, including for a
            'change_requested' item, which closes out via a new version instead of this.
        created_by (str | Unset): User who created the item Example: 507f1f77bcf86cd799439013.
        actor_name (str | Unset): Display name of who authored the current version (user, API key, or OAuth client name)
            Example: Claude.
        version (int | Unset): Version number Example: 1.
        created_at (datetime.datetime | Unset): Creation timestamp Example: 2024-01-15T10:30:00Z.
        updated_at (datetime.datetime | Unset): Last update timestamp Example: 2024-01-15T10:30:00Z.
        expires_at (datetime.datetime | Unset): Expiration timestamp (optional) Example: 2024-02-15T10:30:00Z.
        versions (list[ItemVersion] | Unset): Array of all versions (only if includeVersions=true)
        idempotency_key (str | Unset): The idempotency key the item was created with, if any Example: run-42-review-1.
    """

    id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    title: str | Unset = UNSET
    description: str | Unset = UNSET
    content: ItemContent | Unset = UNSET
    media: list[AttachedMedia] | Unset = UNSET
    metadata: ItemMetadata | Unset = UNSET
    status: ItemStatus | Unset = UNSET
    decisions: list[ItemDecision] | Unset = UNSET
    processed: ItemProcessed | None | Unset = UNSET
    created_by: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    version: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    versions: list[ItemVersion] | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_processed import ItemProcessed  # noqa: PLC0415

        id = self.id

        project_id = self.project_id

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

        processed: dict[str, Any] | None | Unset
        if isinstance(self.processed, Unset):
            processed = UNSET
        elif isinstance(self.processed, ItemProcessed):
            processed = self.processed.to_dict()
        else:
            processed = self.processed

        created_by = self.created_by

        actor_name = self.actor_name

        version = self.version

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
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
        if processed is not UNSET:
            field_dict["processed"] = processed
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name
        if version is not UNSET:
            field_dict["version"] = version
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if versions is not UNSET:
            field_dict["versions"] = versions
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_media import AttachedMedia  # noqa: PLC0415
        from ..models.item_content import ItemContent  # noqa: PLC0415
        from ..models.item_decision import ItemDecision  # noqa: PLC0415
        from ..models.item_metadata import ItemMetadata  # noqa: PLC0415
        from ..models.item_processed import ItemProcessed  # noqa: PLC0415
        from ..models.item_version import ItemVersion  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

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
        metadata: ItemMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ItemMetadata.from_dict(_metadata)

        _status = d.pop("status", UNSET)
        status: ItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ItemStatus(_status)

        _decisions = d.pop("decisions", UNSET)
        decisions: list[ItemDecision] | Unset = UNSET
        if _decisions is not UNSET:
            decisions = []
            for decisions_item_data in _decisions:
                decisions_item = ItemDecision.from_dict(decisions_item_data)

                decisions.append(decisions_item)

        def _parse_processed(data: object) -> ItemProcessed | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                processed_type_1 = ItemProcessed.from_dict(data)

                return processed_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemProcessed | None | Unset, data)

        processed = _parse_processed(d.pop("processed", UNSET))

        created_by = d.pop("createdBy", UNSET)

        actor_name = d.pop("actorName", UNSET)

        version = d.pop("version", UNSET)

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

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _versions = d.pop("versions", UNSET)
        versions: list[ItemVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = ItemVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        item = cls(
            id=id,
            project_id=project_id,
            title=title,
            description=description,
            content=content,
            media=media,
            metadata=metadata,
            status=status,
            decisions=decisions,
            processed=processed,
            created_by=created_by,
            actor_name=actor_name,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
            expires_at=expires_at,
            versions=versions,
            idempotency_key=idempotency_key,
        )

        item.additional_properties = d
        return item

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
