from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_event import AuditEvent


T = TypeVar("T", bound="AuditEventPage")


@_attrs_define
class AuditEventPage:
    """
    Attributes:
        data (list[AuditEvent] | Unset):
        next_cursor (None | str | Unset): Opaque cursor for the next page, or null when there are no more events
            Example: MjAyNC0wMS0xNVQxMDozMDowMC4wMDBafDUwN2YxZjc3YmNmODZjZDc5OTQzOTAxMQ.
        has_more (bool | Unset):  Example: True.
    """

    data: list[AuditEvent] | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event import AuditEvent  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[AuditEvent] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AuditEvent.from_dict(data_item_data)

                data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        has_more = d.pop("hasMore", UNSET)

        audit_event_page = cls(
            data=data,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        audit_event_page.additional_properties = d
        return audit_event_page

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
