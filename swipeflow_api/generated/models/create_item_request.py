from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_item_request_metadata import CreateItemRequestMetadata
    from ..models.item_content import ItemContent


T = TypeVar("T", bound="CreateItemRequest")


@_attrs_define
class CreateItemRequest:
    """
    Attributes:
        title (str): Item title Example: New Content Item.
        description (str | Unset): Item description Example: Description of the content item.
        content (ItemContent | Unset):
        media (list[str] | Unset): Media ids to attach (from `POST .../media-uploads/:id/confirm`). Not inferred from
            `content` — any ref actually embedded in `content.data` is included automatically regardless of this field, but
            an attachment that isn't embedded inline only exists because it's listed here.
             Example: ['66f1f77bcf86cd799439099'].
        metadata (CreateItemRequestMetadata | Unset): Custom metadata Example: {'author': 'John Doe', 'tags': ['tech',
            'api']}.
        idempotency_key (str | Unset): Client-supplied key for safe retries, scoped to the project. Replaying a create
            request with the same key returns the original item rather than creating a duplicate. Must contain a non-
            whitespace character. Example: run-42-review-1.
    """

    title: str
    description: str | Unset = UNSET
    content: ItemContent | Unset = UNSET
    media: list[str] | Unset = UNSET
    metadata: CreateItemRequestMetadata | Unset = UNSET
    idempotency_key: str | Unset = UNSET
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

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if content is not UNSET:
            field_dict["content"] = content
        if media is not UNSET:
            field_dict["media"] = media
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if idempotency_key is not UNSET:
            field_dict["idempotencyKey"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_item_request_metadata import (
            CreateItemRequestMetadata,  # noqa: PLC0415
        )
        from ..models.item_content import ItemContent  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        description = d.pop("description", UNSET)

        _content = d.pop("content", UNSET)
        content: ItemContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ItemContent.from_dict(_content)

        media = cast(list[str], d.pop("media", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateItemRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateItemRequestMetadata.from_dict(_metadata)

        idempotency_key = d.pop("idempotencyKey", UNSET)

        create_item_request = cls(
            title=title,
            description=description,
            content=content,
            media=media,
            metadata=metadata,
            idempotency_key=idempotency_key,
        )

        create_item_request.additional_properties = d
        return create_item_request

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
