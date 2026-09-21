from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.register_device_request_device_type import RegisterDeviceRequestDeviceType

T = TypeVar("T", bound="RegisterDeviceRequest")


@_attrs_define
class RegisterDeviceRequest:
    """
    Attributes:
        device_token (str): Device push notification token Example: ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx].
        device_type (RegisterDeviceRequestDeviceType): Device platform Example: ios.
        device_name (str): Device name Example: iPhone 13.
    """

    device_token: str
    device_type: RegisterDeviceRequestDeviceType
    device_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_token = self.device_token

        device_type = self.device_type.value

        device_name = self.device_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceToken": device_token,
                "deviceType": device_type,
                "deviceName": device_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_token = d.pop("deviceToken")

        device_type = RegisterDeviceRequestDeviceType(d.pop("deviceType"))

        device_name = d.pop("deviceName")

        register_device_request = cls(
            device_token=device_token,
            device_type=device_type,
            device_name=device_name,
        )

        register_device_request.additional_properties = d
        return register_device_request

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
