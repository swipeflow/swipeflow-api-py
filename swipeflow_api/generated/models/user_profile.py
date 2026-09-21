from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_profile_membership import UserProfileMembership
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_address import UserAddress


T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """
    Attributes:
        id (str | Unset): User ID Example: 507f1f77bcf86cd799439011.
        email (str | Unset): User's email address Example: user@example.com.
        first_name (str | Unset): User's first name Example: John.
        last_name (str | Unset): User's last name Example: Doe.
        picture (str | Unset): URL to user's profile picture Example: https://example.com/profile.jpg.
        phone_number (str | Unset): User's phone number Example: 1234567890.
        country (str | Unset): ISO 3166-1 alpha-2 country of the user, independent of the address Example: US.
        address (UserAddress | Unset):
        membership (UserProfileMembership | Unset): User's membership tier Example: pro.
        email_verified (bool | Unset): Whether email is verified Example: True.
        is_admin (bool | Unset): Indicates whether the user has administrative privileges. Used for UI purposes only —
            all admin actions are validated server-side.
             Example: False.
        created_at (datetime.datetime | Unset): Account creation timestamp Example: 2024-01-01T00:00:00Z.
        first_login_at (datetime.datetime | Unset): First login timestamp Example: 2024-01-01T00:00:00Z.
        last_login_at (datetime.datetime | Unset): Last login timestamp Example: 2024-01-01T00:00:00Z.
    """

    id: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    picture: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    country: str | Unset = UNSET
    address: UserAddress | Unset = UNSET
    membership: UserProfileMembership | Unset = UNSET
    email_verified: bool | Unset = UNSET
    is_admin: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    first_login_at: datetime.datetime | Unset = UNSET
    last_login_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        picture = self.picture

        phone_number = self.phone_number

        country = self.country

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        membership: str | Unset = UNSET
        if not isinstance(self.membership, Unset):
            membership = self.membership.value

        email_verified = self.email_verified

        is_admin = self.is_admin

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        first_login_at: str | Unset = UNSET
        if not isinstance(self.first_login_at, Unset):
            first_login_at = self.first_login_at.isoformat()

        last_login_at: str | Unset = UNSET
        if not isinstance(self.last_login_at, Unset):
            last_login_at = self.last_login_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if picture is not UNSET:
            field_dict["picture"] = picture
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if country is not UNSET:
            field_dict["country"] = country
        if address is not UNSET:
            field_dict["address"] = address
        if membership is not UNSET:
            field_dict["membership"] = membership
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if first_login_at is not UNSET:
            field_dict["firstLoginAt"] = first_login_at
        if last_login_at is not UNSET:
            field_dict["lastLoginAt"] = last_login_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_address import UserAddress  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        picture = d.pop("picture", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        country = d.pop("country", UNSET)

        _address = d.pop("address", UNSET)
        address: UserAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = UserAddress.from_dict(_address)

        _membership = d.pop("membership", UNSET)
        membership: UserProfileMembership | Unset
        if isinstance(_membership, Unset):
            membership = UNSET
        else:
            membership = UserProfileMembership(_membership)

        email_verified = d.pop("emailVerified", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _first_login_at = d.pop("firstLoginAt", UNSET)
        first_login_at: datetime.datetime | Unset
        if isinstance(_first_login_at, Unset):
            first_login_at = UNSET
        else:
            first_login_at = datetime.datetime.fromisoformat(_first_login_at)

        _last_login_at = d.pop("lastLoginAt", UNSET)
        last_login_at: datetime.datetime | Unset
        if isinstance(_last_login_at, Unset):
            last_login_at = UNSET
        else:
            last_login_at = datetime.datetime.fromisoformat(_last_login_at)

        user_profile = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            picture=picture,
            phone_number=phone_number,
            country=country,
            address=address,
            membership=membership,
            email_verified=email_verified,
            is_admin=is_admin,
            created_at=created_at,
            first_login_at=first_login_at,
            last_login_at=last_login_at,
        )

        user_profile.additional_properties = d
        return user_profile

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
