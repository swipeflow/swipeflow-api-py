from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectSettingsRequest")


@_attrs_define
class UpdateProjectSettingsRequest:
    """
    Attributes:
        is_archived (bool | Unset): Archive status Example: False.
        is_starred (bool | Unset): Starred status Example: True.
    """

    is_archived: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_archived = self.is_archived

        is_starred = self.is_starred

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if is_starred is not UNSET:
            field_dict["isStarred"] = is_starred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_archived = d.pop("isArchived", UNSET)

        is_starred = d.pop("isStarred", UNSET)

        update_project_settings_request = cls(
            is_archived=is_archived,
            is_starred=is_starred,
        )

        update_project_settings_request.additional_properties = d
        return update_project_settings_request

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
