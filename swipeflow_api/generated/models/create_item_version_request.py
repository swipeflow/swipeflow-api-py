from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_item_version_request_metadata import (
        CreateItemVersionRequestMetadata,
    )
    from ..models.item_content import ItemContent


T = TypeVar("T", bound="CreateItemVersionRequest")


@_attrs_define
class CreateItemVersionRequest:
    """
    Attributes:
        title (str | Unset): Updated item title Example: New Version Title.
        description (str | Unset): Updated item description Example: New version description.
        content (ItemContent | Unset):
        media (list[str] | Unset): Media ids to attach to the new version. Omit to carry over the previous version's
            media exactly, including when `content` is also changing — media is never inferred from a content change. Pass
            `[]` to explicitly detach everything, or a new list to replace it — any ref embedded in *this request's*
            `content` is included automatically regardless of this field, but a ref only present in the *previous*
            (unchanged, carried-over) content is not rescanned, so `[]` reliably detaches even if old content still mentions
            something.
             Example: ['66f1f77bcf86cd799439099'].
        metadata (CreateItemVersionRequestMetadata | Unset): Updated item metadata Example: {'author': 'Jane Doe',
            'version': '2.0'}.
    """

    title: str | Unset = UNSET
    description: str | Unset = UNSET
    content: ItemContent | Unset = UNSET
    media: list[str] | Unset = UNSET
    metadata: CreateItemVersionRequestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        description = self.description

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        media: list[str] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if content is not UNSET:
            field_dict["content"] = content
        if media is not UNSET:
            field_dict["media"] = media
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_item_version_request_metadata import (
            CreateItemVersionRequestMetadata,  # noqa: PLC0415
        )
        from ..models.item_content import ItemContent  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        _content = d.pop("content", UNSET)
        content: ItemContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ItemContent.from_dict(_content)

        media = cast(list[str], d.pop("media", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateItemVersionRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateItemVersionRequestMetadata.from_dict(_metadata)

        create_item_version_request = cls(
            title=title,
            description=description,
            content=content,
            media=media,
            metadata=metadata,
        )

        create_item_version_request.additional_properties = d
        return create_item_version_request

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
