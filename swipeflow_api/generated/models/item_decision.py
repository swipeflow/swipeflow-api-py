from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.decision_type import DecisionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemDecision")


@_attrs_define
class ItemDecision:
    """
    Attributes:
        user_id (str | Unset): User who made the decision Example: 507f1f77bcf86cd799439011.
        decision (DecisionType | Unset): Type of decision made on an item Example: approved.
        comment (str | Unset): Optional comment for the decision Example: Looks good!.
        timestamp (datetime.datetime | Unset): When the decision was made Example: 2024-01-15T10:30:00Z.
        target_version (int | Unset): Target version for change request (only present when decision is
            'change_requested') Example: 1.
        actor_name (str | Unset): Display name of who made the decision — the user, or the API key / OAuth client name
            when acting on their behalf Example: Zapier.
    """

    user_id: str | Unset = UNSET
    decision: DecisionType | Unset = UNSET
    comment: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    target_version: int | Unset = UNSET
    actor_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        decision: str | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.value

        comment = self.comment

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        target_version = self.target_version

        actor_name = self.actor_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if decision is not UNSET:
            field_dict["decision"] = decision
        if comment is not UNSET:
            field_dict["comment"] = comment
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if target_version is not UNSET:
            field_dict["targetVersion"] = target_version
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        _decision = d.pop("decision", UNSET)
        decision: DecisionType | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = DecisionType(_decision)

        comment = d.pop("comment", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        target_version = d.pop("targetVersion", UNSET)

        actor_name = d.pop("actorName", UNSET)

        item_decision = cls(
            user_id=user_id,
            decision=decision,
            comment=comment,
            timestamp=timestamp,
            target_version=target_version,
            actor_name=actor_name,
        )

        item_decision.additional_properties = d
        return item_decision

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
