from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_descriptor_status import MediaDescriptorStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_media_upload_response_201_upload import (
        CreateMediaUploadResponse201Upload,
    )


T = TypeVar("T", bound="CreateMediaUploadResponse201")


@_attrs_define
class CreateMediaUploadResponse201:
    """
    Attributes:
        id (str | Unset):  Example: 66f1f77bcf86cd799439099.
        file_name (str | Unset):  Example: chart.png.
        content_type (str | Unset):  Example: image/png.
        size (int | Unset):  Example: 245678.
        url (None | str | Unset): Signed URL for the bytes, once uploaded. Do not cache or persist it.
        url_expires_at (datetime.datetime | None | Unset): Absolute expiry for `url`. Every row in one response shares
            the same value.
        project_id (str | Unset):  Example: 507f1f77bcf86cd799439012.
        status (MediaDescriptorStatus | Unset):
        created_at (datetime.datetime | Unset):
        uploaded_at (datetime.datetime | None | Unset):
        uploaded_by (str | Unset): The user who uploaded the bytes — provenance only
        item_ids (list[str] | Unset): Items and item versions this object is attached to. Reusable across them within
            the project.
        etag (None | str | Unset): Opaque storage fingerprint — not a portable MD5 guarantee.
        md5 (None | str | Unset): Base64 MD5
        import_error (None | str | Unset): Sanitized terminal failure detail for a URL import, retained for diagnosis.
        import_error_code (None | str | Unset): Stable machine-readable URL-import failure code; use this instead of
            parsing importError.
        import_failed_at (datetime.datetime | None | Unset):
        upload (CreateMediaUploadResponse201Upload | Unset):
    """

    id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    content_type: str | Unset = UNSET
    size: int | Unset = UNSET
    url: None | str | Unset = UNSET
    url_expires_at: datetime.datetime | None | Unset = UNSET
    project_id: str | Unset = UNSET
    status: MediaDescriptorStatus | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    uploaded_at: datetime.datetime | None | Unset = UNSET
    uploaded_by: str | Unset = UNSET
    item_ids: list[str] | Unset = UNSET
    etag: None | str | Unset = UNSET
    md5: None | str | Unset = UNSET
    import_error: None | str | Unset = UNSET
    import_error_code: None | str | Unset = UNSET
    import_failed_at: datetime.datetime | None | Unset = UNSET
    upload: CreateMediaUploadResponse201Upload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name = self.file_name

        content_type = self.content_type

        size = self.size

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_expires_at: None | str | Unset
        if isinstance(self.url_expires_at, Unset):
            url_expires_at = UNSET
        elif isinstance(self.url_expires_at, datetime.datetime):
            url_expires_at = self.url_expires_at.isoformat()
        else:
            url_expires_at = self.url_expires_at

        project_id = self.project_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        uploaded_at: None | str | Unset
        if isinstance(self.uploaded_at, Unset):
            uploaded_at = UNSET
        elif isinstance(self.uploaded_at, datetime.datetime):
            uploaded_at = self.uploaded_at.isoformat()
        else:
            uploaded_at = self.uploaded_at

        uploaded_by = self.uploaded_by

        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        md5: None | str | Unset
        if isinstance(self.md5, Unset):
            md5 = UNSET
        else:
            md5 = self.md5

        import_error: None | str | Unset
        if isinstance(self.import_error, Unset):
            import_error = UNSET
        else:
            import_error = self.import_error

        import_error_code: None | str | Unset
        if isinstance(self.import_error_code, Unset):
            import_error_code = UNSET
        else:
            import_error_code = self.import_error_code

        import_failed_at: None | str | Unset
        if isinstance(self.import_failed_at, Unset):
            import_failed_at = UNSET
        elif isinstance(self.import_failed_at, datetime.datetime):
            import_failed_at = self.import_failed_at.isoformat()
        else:
            import_failed_at = self.import_failed_at

        upload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upload, Unset):
            upload = self.upload.to_dict()

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
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if uploaded_at is not UNSET:
            field_dict["uploadedAt"] = uploaded_at
        if uploaded_by is not UNSET:
            field_dict["uploadedBy"] = uploaded_by
        if item_ids is not UNSET:
            field_dict["itemIds"] = item_ids
        if etag is not UNSET:
            field_dict["etag"] = etag
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if import_error is not UNSET:
            field_dict["importError"] = import_error
        if import_error_code is not UNSET:
            field_dict["importErrorCode"] = import_error_code
        if import_failed_at is not UNSET:
            field_dict["importFailedAt"] = import_failed_at
        if upload is not UNSET:
            field_dict["upload"] = upload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_media_upload_response_201_upload import (
            CreateMediaUploadResponse201Upload,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        file_name = d.pop("fileName", UNSET)

        content_type = d.pop("contentType", UNSET)

        size = d.pop("size", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_url_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                url_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return url_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        url_expires_at = _parse_url_expires_at(d.pop("urlExpiresAt", UNSET))

        project_id = d.pop("projectId", UNSET)

        _status = d.pop("status", UNSET)
        status: MediaDescriptorStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MediaDescriptorStatus(_status)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_uploaded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uploaded_at_type_0 = datetime.datetime.fromisoformat(data)

                return uploaded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        uploaded_at = _parse_uploaded_at(d.pop("uploadedAt", UNSET))

        uploaded_by = d.pop("uploadedBy", UNSET)

        item_ids = cast(list[str], d.pop("itemIds", UNSET))

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_md5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        md5 = _parse_md5(d.pop("md5", UNSET))

        def _parse_import_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_error = _parse_import_error(d.pop("importError", UNSET))

        def _parse_import_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_error_code = _parse_import_error_code(d.pop("importErrorCode", UNSET))

        def _parse_import_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                import_failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return import_failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        import_failed_at = _parse_import_failed_at(d.pop("importFailedAt", UNSET))

        _upload = d.pop("upload", UNSET)
        upload: CreateMediaUploadResponse201Upload | Unset
        if isinstance(_upload, Unset):
            upload = UNSET
        else:
            upload = CreateMediaUploadResponse201Upload.from_dict(_upload)

        create_media_upload_response_201 = cls(
            id=id,
            file_name=file_name,
            content_type=content_type,
            size=size,
            url=url,
            url_expires_at=url_expires_at,
            project_id=project_id,
            status=status,
            created_at=created_at,
            uploaded_at=uploaded_at,
            uploaded_by=uploaded_by,
            item_ids=item_ids,
            etag=etag,
            md5=md5,
            import_error=import_error,
            import_error_code=import_error_code,
            import_failed_at=import_failed_at,
            upload=upload,
        )

        create_media_upload_response_201.additional_properties = d
        return create_media_upload_response_201

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
