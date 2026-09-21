from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UpdateUserProfilePictureBody")


@_attrs_define
class UpdateUserProfilePictureBody:
    """
    Attributes:
        picture (File | Unset): Profile picture file (max 5MB, image files only - will be converted to PNG)
    """

    picture: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        picture: FileTypes | Unset = UNSET
        if not isinstance(self.picture, Unset):
            picture = self.picture.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if picture is not UNSET:
            field_dict["picture"] = picture

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.picture, Unset):
            files.append(("picture", self.picture.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _picture = d.pop("picture", UNSET)
        picture: File | Unset
        if isinstance(_picture, Unset):
            picture = UNSET
        else:
            picture = File(payload=BytesIO(_picture))

        update_user_profile_picture_body = cls(
            picture=picture,
        )

        update_user_profile_picture_body.additional_properties = d
        return update_user_profile_picture_body

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
