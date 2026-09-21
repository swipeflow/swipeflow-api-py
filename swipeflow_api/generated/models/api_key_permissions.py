from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKeyPermissions")


@_attrs_define
class APIKeyPermissions:
    """
    Attributes:
        read (bool | Unset): Read permission Example: True.
        write (bool | Unset): Write permission Example: False.
        project_ids (list[str] | None | Unset): Allowed project IDs (null means all projects) Example:
            ['507f1f77bcf86cd799439011', '507f1f77bcf86cd799439012'].
    """

    read: bool | Unset = UNSET
    write: bool | Unset = UNSET
    project_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read = self.read

        write = self.write

        project_ids: list[str] | None | Unset
        if isinstance(self.project_ids, Unset):
            project_ids = UNSET
        elif isinstance(self.project_ids, list):
            project_ids = self.project_ids

        else:
            project_ids = self.project_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read is not UNSET:
            field_dict["read"] = read
        if write is not UNSET:
            field_dict["write"] = write
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read", UNSET)

        write = d.pop("write", UNSET)

        def _parse_project_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_ids_type_0 = cast(list[str], data)

                return project_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        project_ids = _parse_project_ids(d.pop("projectIds", UNSET))

        api_key_permissions = cls(
            read=read,
            write=write,
            project_ids=project_ids,
        )

        api_key_permissions.additional_properties = d
        return api_key_permissions

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
