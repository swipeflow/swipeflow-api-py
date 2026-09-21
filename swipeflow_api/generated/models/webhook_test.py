from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTest")


@_attrs_define
class WebhookTest:
    """
    Attributes:
        success (bool | Unset): Whether the test was successful Example: True.
        message (str | Unset): Test result message Example: Webhook test successful.
        status_code (int | Unset): HTTP status code from webhook endpoint Example: 200.
    """

    success: bool | Unset = UNSET
    message: str | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        status_code = d.pop("statusCode", UNSET)

        webhook_test = cls(
            success=success,
            message=message,
            status_code=status_code,
        )

        webhook_test.additional_properties = d
        return webhook_test

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
