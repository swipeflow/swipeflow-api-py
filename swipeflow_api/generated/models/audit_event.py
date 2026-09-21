from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_event_type import AuditEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_event_actor import AuditEventActor
    from ..models.audit_event_context_type_0 import AuditEventContextType0
    from ..models.audit_event_metadata_type_0 import AuditEventMetadataType0
    from ..models.audit_event_target import AuditEventTarget


T = TypeVar("T", bound="AuditEvent")


@_attrs_define
class AuditEvent:
    """
    Attributes:
        id (str | Unset):  Example: 507f1f77bcf86cd799439011.
        type_ (AuditEventType | Unset): Type of a recorded audit event. COMMENT_* and USER_LOGIN* values are reserved
            and not emitted yet.
             Example: ITEM_APPROVED.
        actor (AuditEventActor | Unset):
        project_id (None | str | Unset):  Example: 507f1f77bcf86cd799439011.
        subject_user_id (None | str | Unset): The user this event is about, when distinct from the actor Example:
            507f1f77bcf86cd799439011.
        target (AuditEventTarget | Unset):
        metadata (AuditEventMetadataType0 | None | Unset): Event-specific detail. Never contains secrets.
        related_project_ids (list[str] | None | Unset): Projects an API-key event is relevant to, even though the event
            has no `projectId`: the key's explicit permission scope, or — for an unscoped key — the owner's project
            memberships at the time of the event.
        context (AuditEventContextType0 | None | Unset): Request context. Included for the caller's own feed and the
            admin feed; on a project feed only for a platform admin or the project's OWNER/ADMIN.
        created_at (datetime.datetime | Unset): When the event was recorded, in UTC (ISO 8601, e.g.
            `2024-01-15T10:30:00.000Z`). Millisecond precision. Example: 2024-01-15T10:30:00.000Z.
    """

    id: str | Unset = UNSET
    type_: AuditEventType | Unset = UNSET
    actor: AuditEventActor | Unset = UNSET
    project_id: None | str | Unset = UNSET
    subject_user_id: None | str | Unset = UNSET
    target: AuditEventTarget | Unset = UNSET
    metadata: AuditEventMetadataType0 | None | Unset = UNSET
    related_project_ids: list[str] | None | Unset = UNSET
    context: AuditEventContextType0 | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_event_context_type_0 import (
            AuditEventContextType0,  # noqa: PLC0415
        )
        from ..models.audit_event_metadata_type_0 import (
            AuditEventMetadataType0,  # noqa: PLC0415
        )

        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        subject_user_id: None | str | Unset
        if isinstance(self.subject_user_id, Unset):
            subject_user_id = UNSET
        else:
            subject_user_id = self.subject_user_id

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AuditEventMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        related_project_ids: list[str] | None | Unset
        if isinstance(self.related_project_ids, Unset):
            related_project_ids = UNSET
        elif isinstance(self.related_project_ids, list):
            related_project_ids = self.related_project_ids

        else:
            related_project_ids = self.related_project_ids

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, AuditEventContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if actor is not UNSET:
            field_dict["actor"] = actor
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if subject_user_id is not UNSET:
            field_dict["subjectUserId"] = subject_user_id
        if target is not UNSET:
            field_dict["target"] = target
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if related_project_ids is not UNSET:
            field_dict["relatedProjectIds"] = related_project_ids
        if context is not UNSET:
            field_dict["context"] = context
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event_actor import AuditEventActor  # noqa: PLC0415
        from ..models.audit_event_context_type_0 import (
            AuditEventContextType0,  # noqa: PLC0415
        )
        from ..models.audit_event_metadata_type_0 import (
            AuditEventMetadataType0,  # noqa: PLC0415
        )
        from ..models.audit_event_target import AuditEventTarget  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AuditEventType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AuditEventType(_type_)

        _actor = d.pop("actor", UNSET)
        actor: AuditEventActor | Unset
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = AuditEventActor.from_dict(_actor)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_subject_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_user_id = _parse_subject_user_id(d.pop("subjectUserId", UNSET))

        _target = d.pop("target", UNSET)
        target: AuditEventTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = AuditEventTarget.from_dict(_target)

        def _parse_metadata(data: object) -> AuditEventMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AuditEventMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditEventMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_related_project_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                related_project_ids_type_0 = cast(list[str], data)

                return related_project_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        related_project_ids = _parse_related_project_ids(
            d.pop("relatedProjectIds", UNSET)
        )

        def _parse_context(data: object) -> AuditEventContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = AuditEventContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditEventContextType0 | None | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        audit_event = cls(
            id=id,
            type_=type_,
            actor=actor,
            project_id=project_id,
            subject_user_id=subject_user_id,
            target=target,
            metadata=metadata,
            related_project_ids=related_project_ids,
            context=context,
            created_at=created_at,
        )

        audit_event.additional_properties = d
        return audit_event

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
