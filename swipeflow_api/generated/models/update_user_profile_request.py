from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_address import UserAddress


T = TypeVar("T", bound="UpdateUserProfileRequest")


@_attrs_define
class UpdateUserProfileRequest:
    """
    Attributes:
        first_name (str | Unset): User's first name Example: John.
        last_name (str | Unset): User's last name Example: Doe.
        phone_number (str | Unset): User's phone number Example: 1234567890.
        country (str | Unset): ISO 3166-1 alpha-2 country of the user, independent of the address Example: US.
        address (UserAddress | Unset):
    """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    country: str | Unset = UNSET
    address: UserAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        phone_number = self.phone_number

        country = self.country

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if country is not UNSET:
            field_dict["country"] = country
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_address import UserAddress  # noqa: PLC0415

        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        country = d.pop("country", UNSET)

        _address = d.pop("address", UNSET)
        address: UserAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = UserAddress.from_dict(_address)

        update_user_profile_request = cls(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            country=country,
            address=address,
        )

        update_user_profile_request.additional_properties = d
        return update_user_profile_request

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
