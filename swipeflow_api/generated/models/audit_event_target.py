from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_event_target_type import AuditEventTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditEventTarget")


@_attrs_define
class AuditEventTarget:
    """
    Attributes:
        type_ (AuditEventTargetType | Unset):  Example: item.
        id (str | Unset):  Example: 507f1f77bcf86cd799439011.
        display_name (None | str | Unset):  Example: Q3 launch announcement.
    """

    type_: AuditEventTargetType | Unset = UNSET
    id: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: AuditEventTargetType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AuditEventTargetType(_type_)

        id = d.pop("id", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        audit_event_target = cls(
            type_=type_,
            id=id,
            display_name=display_name,
        )

        audit_event_target.additional_properties = d
        return audit_event_target

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
