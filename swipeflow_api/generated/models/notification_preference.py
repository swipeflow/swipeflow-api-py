from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery_method import DeliveryMethod
from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationPreference")


@_attrs_define
class NotificationPreference:
    """
    Attributes:
        type_ (NotificationType | Unset): Type of notification Example: ITEM_CREATED.
        methods (list[DeliveryMethod] | Unset): Delivery methods Example: ['PUSH', 'EMAIL'].
        enabled (bool | Unset): Whether notification is enabled Example: True.
    """

    type_: NotificationType | Unset = UNSET
    methods: list[DeliveryMethod] | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        methods: list[str] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.value
                methods.append(methods_item)

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if methods is not UNSET:
            field_dict["methods"] = methods
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: NotificationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NotificationType(_type_)

        _methods = d.pop("methods", UNSET)
        methods: list[DeliveryMethod] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = DeliveryMethod(methods_item_data)

                methods.append(methods_item)

        enabled = d.pop("enabled", UNSET)

        notification_preference = cls(
            type_=type_,
            methods=methods,
            enabled=enabled,
        )

        notification_preference.additional_properties = d
        return notification_preference

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
