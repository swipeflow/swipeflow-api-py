from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_user_storage_use_response_200_plan import (
    GetUserStorageUseResponse200Plan,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_user_storage_use_response_200_media import (
        GetUserStorageUseResponse200Media,
    )


T = TypeVar("T", bound="GetUserStorageUseResponse200")


@_attrs_define
class GetUserStorageUseResponse200:
    """
    Attributes:
        limit_bytes (int | Unset):
        plan (GetUserStorageUseResponse200Plan | Unset):
        seats (int | Unset):
        used_bytes (int | Unset):
        media (GetUserStorageUseResponse200Media | Unset):
    """

    limit_bytes: int | Unset = UNSET
    plan: GetUserStorageUseResponse200Plan | Unset = UNSET
    seats: int | Unset = UNSET
    used_bytes: int | Unset = UNSET
    media: GetUserStorageUseResponse200Media | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_bytes = self.limit_bytes

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        seats = self.seats

        used_bytes = self.used_bytes

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit_bytes is not UNSET:
            field_dict["limitBytes"] = limit_bytes
        if plan is not UNSET:
            field_dict["plan"] = plan
        if seats is not UNSET:
            field_dict["seats"] = seats
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_user_storage_use_response_200_media import (
            GetUserStorageUseResponse200Media,  # noqa: PLC0415
        )

        d = dict(src_dict)
        limit_bytes = d.pop("limitBytes", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: GetUserStorageUseResponse200Plan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = GetUserStorageUseResponse200Plan(_plan)

        seats = d.pop("seats", UNSET)

        used_bytes = d.pop("usedBytes", UNSET)

        _media = d.pop("media", UNSET)
        media: GetUserStorageUseResponse200Media | Unset
        if isinstance(_media, Unset):
            media = UNSET
        else:
            media = GetUserStorageUseResponse200Media.from_dict(_media)

        get_user_storage_use_response_200 = cls(
            limit_bytes=limit_bytes,
            plan=plan,
            seats=seats,
            used_bytes=used_bytes,
            media=media,
        )

        get_user_storage_use_response_200.additional_properties = d
        return get_user_storage_use_response_200

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
