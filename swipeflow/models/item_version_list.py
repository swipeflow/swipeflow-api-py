from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_version import ItemVersion
    from ..models.pagination_meta import PaginationMeta


T = TypeVar("T", bound="ItemVersionList")


@_attrs_define
class ItemVersionList:
    """
    Attributes:
        versions (list[ItemVersion] | Unset):
        pagination (PaginationMeta | Unset):
    """

    versions: list[ItemVersion] | Unset = UNSET
    pagination: PaginationMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if versions is not UNSET:
            field_dict["versions"] = versions
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_version import ItemVersion  # noqa: PLC0415
        from ..models.pagination_meta import PaginationMeta  # noqa: PLC0415

        d = dict(src_dict)
        _versions = d.pop("versions", UNSET)
        versions: list[ItemVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = ItemVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: PaginationMeta | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationMeta.from_dict(_pagination)

        item_version_list = cls(
            versions=versions,
            pagination=pagination,
        )

        item_version_list.additional_properties = d
        return item_version_list

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
