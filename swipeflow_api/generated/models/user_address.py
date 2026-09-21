from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAddress")


@_attrs_define
class UserAddress:
    """
    Attributes:
        street (str | Unset):  Example: 123 Main St.
        city (str | Unset):  Example: San Francisco.
        state (str | Unset):  Example: CA.
        postal_code (str | Unset):  Example: 94102.
        country (str | Unset): ISO 3166-1 alpha-2 country the post goes to Example: US.
    """

    street: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street = self.street

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        user_address = cls(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )

        user_address.additional_properties = d
        return user_address

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
