from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_type import ContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemContent")


@_attrs_define
class ItemContent:
    """
    Attributes:
        type_ (ContentType | Unset): Type of content in an item Example: text.
        data (str | Unset): For text/html: the content itself, which may embed one or more canonical `media://<id>` refs
            inline — e.g. markdown `![alt](media://66f1f77bcf86cd799439099)`. For image/video/audio: a single media ref, or
            an external https URL. Refs are **not** substituted for a live URL here unless the request opted in with
            `resolveMedia=true` — see `media[]` for why.
             Example: This is sample content.
    """

    type_: ContentType | Unset = UNSET
    data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ContentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContentType(_type_)

        data = d.pop("data", UNSET)

        item_content = cls(
            type_=type_,
            data=data,
        )

        item_content.additional_properties = d
        return item_content

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
