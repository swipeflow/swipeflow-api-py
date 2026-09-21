from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination_meta import PaginationMeta
    from ..models.project import Project


T = TypeVar("T", bound="ProjectList")


@_attrs_define
class ProjectList:
    """
    Attributes:
        projects (list[Project] | Unset):
        pagination (PaginationMeta | Unset):
        favorites (list[Project] | Unset): The caller's starred, non-archived projects. Only present on the unfiltered
            first page.
    """

    projects: list[Project] | Unset = UNSET
    pagination: PaginationMeta | Unset = UNSET
    favorites: list[Project] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        favorites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = []
            for favorites_item_data in self.favorites:
                favorites_item = favorites_item_data.to_dict()
                favorites.append(favorites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if favorites is not UNSET:
            field_dict["favorites"] = favorites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_meta import PaginationMeta  # noqa: PLC0415
        from ..models.project import Project  # noqa: PLC0415

        d = dict(src_dict)
        _projects = d.pop("projects", UNSET)
        projects: list[Project] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = Project.from_dict(projects_item_data)

                projects.append(projects_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: PaginationMeta | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationMeta.from_dict(_pagination)

        _favorites = d.pop("favorites", UNSET)
        favorites: list[Project] | Unset = UNSET
        if _favorites is not UNSET:
            favorites = []
            for favorites_item_data in _favorites:
                favorites_item = Project.from_dict(favorites_item_data)

                favorites.append(favorites_item)

        project_list = cls(
            projects=projects,
            pagination=pagination,
            favorites=favorites,
        )

        project_list.additional_properties = d
        return project_list

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
