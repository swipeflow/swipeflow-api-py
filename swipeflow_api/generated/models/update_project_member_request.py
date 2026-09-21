from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_role import ProjectRole

T = TypeVar("T", bound="UpdateProjectMemberRequest")


@_attrs_define
class UpdateProjectMemberRequest:
    """
    Attributes:
        role (ProjectRole): Role of a member in a project:
            - owner: Project creator, cannot be removed
            - admin: Can manage members and settings
            - editor: Can create and edit items
            - viewer: Read-only access
             Example: editor.
    """

    role: ProjectRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = ProjectRole(d.pop("role"))

        update_project_member_request = cls(
            role=role,
        )

        update_project_member_request.additional_properties = d
        return update_project_member_request

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
