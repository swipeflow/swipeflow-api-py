from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserStorageUseResponse200MediaProjectsItem")


@_attrs_define
class GetUserStorageUseResponse200MediaProjectsItem:
    """
    Attributes:
        project_id (str | Unset):
        used_bytes (int | Unset):
    """

    project_id: str | Unset = UNSET
    used_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        used_bytes = self.used_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectId", UNSET)

        used_bytes = d.pop("usedBytes", UNSET)

        get_user_storage_use_response_200_media_projects_item = cls(
            project_id=project_id,
            used_bytes=used_bytes,
        )

        get_user_storage_use_response_200_media_projects_item.additional_properties = d
        return get_user_storage_use_response_200_media_projects_item

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
