from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_event_actor_actor_type import AuditEventActorActorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditEventActor")


@_attrs_define
class AuditEventActor:
    """
    Attributes:
        actor_type (AuditEventActorActorType | Unset):  Example: user.
        user_id (None | str | Unset): Account the action ran under, when there is one Example: 507f1f77bcf86cd799439011.
        name (str | Unset): Snapshot of the acting party's display name Example: Jane Doe.
        email (None | str | Unset):  Example: jane@example.com.
    """

    actor_type: AuditEventActorActorType | Unset = UNSET
    user_id: None | str | Unset = UNSET
    name: str | Unset = UNSET
    email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_type: str | Unset = UNSET
        if not isinstance(self.actor_type, Unset):
            actor_type = self.actor_type.value

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        name = self.name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actor_type is not UNSET:
            field_dict["actorType"] = actor_type
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _actor_type = d.pop("actorType", UNSET)
        actor_type: AuditEventActorActorType | Unset
        if isinstance(_actor_type, Unset):
            actor_type = UNSET
        else:
            actor_type = AuditEventActorActorType(_actor_type)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        name = d.pop("name", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        audit_event_actor = cls(
            actor_type=actor_type,
            user_id=user_id,
            name=name,
            email=email,
        )

        audit_event_actor.additional_properties = d
        return audit_event_actor

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
