from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMediaUploadBody")


@_attrs_define
class CreateMediaUploadBody:
    """
    Attributes:
        filename (str):
        file_size (int): Exact size in bytes.
        mime_type (str):
        md5 (str | Unset): Optional base64 MD5, validated by storage during the PUT.
    """

    filename: str
    file_size: int
    mime_type: str
    md5: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        file_size = self.file_size

        mime_type = self.mime_type

        md5 = self.md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "fileSize": file_size,
                "mimeType": mime_type,
            }
        )
        if md5 is not UNSET:
            field_dict["md5"] = md5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        file_size = d.pop("fileSize")

        mime_type = d.pop("mimeType")

        md5 = d.pop("md5", UNSET)

        create_media_upload_body = cls(
            filename=filename,
            file_size=file_size,
            mime_type=mime_type,
            md5=md5,
        )

        create_media_upload_body.additional_properties = d
        return create_media_upload_body

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
