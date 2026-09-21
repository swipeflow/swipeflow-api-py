from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemProcessed")


@_attrs_define
class ItemProcessed:
    """Requester-side reconciliation record — proof the decision was actually acted on, not just delivered (by webhook or
    by reading it), and the durable backstop for finding anything a missed or unretried webhook delivery left stranded.

        Attributes:
            processed_at (datetime.datetime | Unset): When the item was marked processed Example: 2024-01-15T11:00:00Z.
            processed_by (str | Unset): User who marked the item processed Example: 507f1f77bcf86cd799439013.
            action (str | Unset): Optional free-text note on what was done with the decision Example: Published to CMS.
            actor_name (str | Unset): Display name of who marked it processed (user, API key, or OAuth client name) Example:
                Claude.
    """

    processed_at: datetime.datetime | Unset = UNSET
    processed_by: str | Unset = UNSET
    action: str | Unset = UNSET
    actor_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed_at: str | Unset = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        processed_by = self.processed_by

        action = self.action

        actor_name = self.actor_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if processed_by is not UNSET:
            field_dict["processedBy"] = processed_by
        if action is not UNSET:
            field_dict["action"] = action
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _processed_at = d.pop("processedAt", UNSET)
        processed_at: datetime.datetime | Unset
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = datetime.datetime.fromisoformat(_processed_at)

        processed_by = d.pop("processedBy", UNSET)

        action = d.pop("action", UNSET)

        actor_name = d.pop("actorName", UNSET)

        item_processed = cls(
            processed_at=processed_at,
            processed_by=processed_by,
            action=action,
            actor_name=actor_name,
        )

        item_processed.additional_properties = d
        return item_processed

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
