from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_storage_use_response_200_media_projects_item import (
        GetUserStorageUseResponse200MediaProjectsItem,
    )


T = TypeVar("T", bound="GetUserStorageUseResponse200Media")


@_attrs_define
class GetUserStorageUseResponse200Media:
    """
    Attributes:
        used_bytes (int | Unset):
        projects (list[GetUserStorageUseResponse200MediaProjectsItem] | Unset):
    """

    used_bytes: int | Unset = UNSET
    projects: list[GetUserStorageUseResponse200MediaProjectsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_bytes = self.used_bytes

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes
        if projects is not UNSET:
            field_dict["projects"] = projects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_user_storage_use_response_200_media_projects_item import (
            GetUserStorageUseResponse200MediaProjectsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        used_bytes = d.pop("usedBytes", UNSET)

        _projects = d.pop("projects", UNSET)
        projects: list[GetUserStorageUseResponse200MediaProjectsItem] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = GetUserStorageUseResponse200MediaProjectsItem.from_dict(
                    projects_item_data
                )

                projects.append(projects_item)

        get_user_storage_use_response_200_media = cls(
            used_bytes=used_bytes,
            projects=projects,
        )

        get_user_storage_use_response_200_media.additional_properties = d
        return get_user_storage_use_response_200_media

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
