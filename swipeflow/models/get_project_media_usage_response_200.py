from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_project_media_usage_response_200_plan import (
    GetProjectMediaUsageResponse200Plan,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectMediaUsageResponse200")


@_attrs_define
class GetProjectMediaUsageResponse200:
    """
    Attributes:
        used_bytes (int | Unset):
        limit_bytes (int | Unset):
        plan (GetProjectMediaUsageResponse200Plan | Unset):
        seats (int | Unset):
    """

    used_bytes: int | Unset = UNSET
    limit_bytes: int | Unset = UNSET
    plan: GetProjectMediaUsageResponse200Plan | Unset = UNSET
    seats: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used_bytes = self.used_bytes

        limit_bytes = self.limit_bytes

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        seats = self.seats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes
        if limit_bytes is not UNSET:
            field_dict["limitBytes"] = limit_bytes
        if plan is not UNSET:
            field_dict["plan"] = plan
        if seats is not UNSET:
            field_dict["seats"] = seats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used_bytes = d.pop("usedBytes", UNSET)

        limit_bytes = d.pop("limitBytes", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: GetProjectMediaUsageResponse200Plan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = GetProjectMediaUsageResponse200Plan(_plan)

        seats = d.pop("seats", UNSET)

        get_project_media_usage_response_200 = cls(
            used_bytes=used_bytes,
            limit_bytes=limit_bytes,
            plan=plan,
            seats=seats,
        )

        get_project_media_usage_response_200.additional_properties = d
        return get_project_media_usage_response_200

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
