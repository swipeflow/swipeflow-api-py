from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_permissions import APIKeyPermissions


T = TypeVar("T", bound="APIKey")


@_attrs_define
class APIKey:
    """
    Attributes:
        id (str | Unset): API key ID Example: 507f1f77bcf86cd799439011.
        name (str | Unset): API key name Example: Production API Key.
        masked_key (str | Unset): Masked API key (only first and last 3 characters visible) Example: abc....xyz.
        permissions (APIKeyPermissions | Unset):
        last_used (datetime.datetime | Unset): Last usage timestamp Example: 2024-01-15T10:30:00Z.
        created_at (datetime.datetime | Unset): Creation timestamp Example: 2024-01-01T00:00:00Z.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    masked_key: str | Unset = UNSET
    permissions: APIKeyPermissions | Unset = UNSET
    last_used: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        masked_key = self.masked_key

        permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        last_used: str | Unset = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if masked_key is not UNSET:
            field_dict["maskedKey"] = masked_key
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_permissions import APIKeyPermissions  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        masked_key = d.pop("maskedKey", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: APIKeyPermissions | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = APIKeyPermissions.from_dict(_permissions)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: datetime.datetime | Unset
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = datetime.datetime.fromisoformat(_last_used)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        api_key = cls(
            id=id,
            name=name,
            masked_key=masked_key,
            permissions=permissions,
            last_used=last_used,
            created_at=created_at,
        )

        api_key.additional_properties = d
        return api_key

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
