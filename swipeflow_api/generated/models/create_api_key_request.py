from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_permissions import APIKeyPermissions


T = TypeVar("T", bound="CreateAPIKeyRequest")


@_attrs_define
class CreateAPIKeyRequest:
    """
    Attributes:
        name (str): Name for the API key Example: My API Key.
        permissions (APIKeyPermissions | Unset):
    """

    name: str
    permissions: APIKeyPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_permissions import APIKeyPermissions  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        _permissions = d.pop("permissions", UNSET)
        permissions: APIKeyPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = APIKeyPermissions.from_dict(_permissions)

        create_api_key_request = cls(
            name=name,
            permissions=permissions,
        )

        create_api_key_request.additional_properties = d
        return create_api_key_request

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
