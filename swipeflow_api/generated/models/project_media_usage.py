from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectMediaUsage")


@_attrs_define
class ProjectMediaUsage:
    """Only present on the single-project detail read (not the list). usedBytes counts this project's pending, uploaded,
    and in-flight-import media — informational; the full quota + limit breakdown is at GET
    /v1/projects/{projectId}/media/usage.

        Attributes:
            used_bytes (int | Unset):  Example: 1048576.
    """

    used_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_bytes = self.used_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used_bytes = d.pop("usedBytes", UNSET)

        project_media_usage = cls(
            used_bytes=used_bytes,
        )

        project_media_usage.additional_properties = d
        return project_media_usage

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
