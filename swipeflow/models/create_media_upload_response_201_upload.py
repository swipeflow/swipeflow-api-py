from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_media_upload_response_201_upload_method import (
    CreateMediaUploadResponse201UploadMethod,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_media_upload_response_201_upload_headers import (
        CreateMediaUploadResponse201UploadHeaders,
    )


T = TypeVar("T", bound="CreateMediaUploadResponse201Upload")


@_attrs_define
class CreateMediaUploadResponse201Upload:
    """
    Attributes:
        url (str | Unset):
        method (CreateMediaUploadResponse201UploadMethod | Unset):
        headers (CreateMediaUploadResponse201UploadHeaders | Unset):
        expires_at (datetime.datetime | Unset):
    """

    url: str | Unset = UNSET
    method: CreateMediaUploadResponse201UploadMethod | Unset = UNSET
    headers: CreateMediaUploadResponse201UploadHeaders | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if method is not UNSET:
            field_dict["method"] = method
        if headers is not UNSET:
            field_dict["headers"] = headers
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_media_upload_response_201_upload_headers import (
            CreateMediaUploadResponse201UploadHeaders,  # noqa: PLC0415
        )

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _method = d.pop("method", UNSET)
        method: CreateMediaUploadResponse201UploadMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = CreateMediaUploadResponse201UploadMethod(_method)

        _headers = d.pop("headers", UNSET)
        headers: CreateMediaUploadResponse201UploadHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = CreateMediaUploadResponse201UploadHeaders.from_dict(_headers)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        create_media_upload_response_201_upload = cls(
            url=url,
            method=method,
            headers=headers,
            expires_at=expires_at,
        )

        create_media_upload_response_201_upload.additional_properties = d
        return create_media_upload_response_201_upload

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
