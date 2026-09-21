from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedMedia")


@_attrs_define
class AttachedMedia:
    """One file attached to an item or item version — either referenced inline in `content.data`, or attached explicitly
    via `media` on create/version-create without necessarily appearing in the content body at all.

        Attributes:
            id (str | Unset): Media id Example: 66f1f77bcf86cd799439099.
            file_name (str | Unset): Original filename, if the uploader gave one Example: chart.png.
            content_type (str | Unset):  Example: image/png.
            size (int | Unset): Size in bytes Example: 245678.
            url (str | Unset): Signed URL for the bytes, always present. Expires at `urlExpiresAt`; do not cache or persist
                it — refetch the containing item/list to refresh. Example: https://abc123.r2.cloudflarestorage.com/swipeflow-
                media/...&X-Amz-Signature=....
            url_expires_at (datetime.datetime | Unset): Absolute expiry for `url`. Every media entry in one response shares
                the same value. Example: 2024-01-15T11:30:00Z.
    """

    id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    content_type: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    url_expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name = self.file_name

        content_type = self.content_type

        size = self.size

        url = self.url

        url_expires_at: str | Unset = UNSET
        if not isinstance(self.url_expires_at, Unset):
            url_expires_at = self.url_expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url
        if url_expires_at is not UNSET:
            field_dict["urlExpiresAt"] = url_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        file_name = d.pop("fileName", UNSET)

        content_type = d.pop("contentType", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        _url_expires_at = d.pop("urlExpiresAt", UNSET)
        url_expires_at: datetime.datetime | Unset
        if isinstance(_url_expires_at, Unset):
            url_expires_at = UNSET
        else:
            url_expires_at = datetime.datetime.fromisoformat(_url_expires_at)

        attached_media = cls(
            id=id,
            file_name=file_name,
            content_type=content_type,
            size=size,
            url=url,
            url_expires_at=url_expires_at,
        )

        attached_media.additional_properties = d
        return attached_media

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
