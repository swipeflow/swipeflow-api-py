from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_role import ProjectRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_user_profile import PublicUserProfile


T = TypeVar("T", bound="ProjectMember")


@_attrs_define
class ProjectMember:
    """
    Attributes:
        role (ProjectRole | Unset): Role of a member in a project:
            - owner: Project creator, cannot be removed
            - admin: Can manage members and settings
            - editor: Can create and edit items
            - viewer: Read-only access
             Example: editor.
        user (PublicUserProfile | Unset):
    """

    role: ProjectRole | Unset = UNSET
    user: PublicUserProfile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_user_profile import PublicUserProfile  # noqa: PLC0415

        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: ProjectRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ProjectRole(_role)

        _user = d.pop("user", UNSET)
        user: PublicUserProfile | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PublicUserProfile.from_dict(_user)

        project_member = cls(
            role=role,
            user=user,
        )

        project_member.additional_properties = d
        return project_member

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
