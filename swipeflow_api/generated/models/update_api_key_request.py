from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_permissions import APIKeyPermissions


T = TypeVar("T", bound="UpdateAPIKeyRequest")


@_attrs_define
class UpdateAPIKeyRequest:
    """Partial update — supply only the fields to change.

    Attributes:
        name (str | Unset):
        permissions (APIKeyPermissions | Unset):
    """

    name: str | Unset = UNSET
    permissions: APIKeyPermissions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_permissions import APIKeyPermissions  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: APIKeyPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = APIKeyPermissions.from_dict(_permissions)

        update_api_key_request = cls(
            name=name,
            permissions=permissions,
        )

        update_api_key_request.additional_properties = d
        return update_api_key_request

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
