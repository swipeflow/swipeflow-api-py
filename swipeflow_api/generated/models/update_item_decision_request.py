from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_item_decision_request_decision import (
    UpdateItemDecisionRequestDecision,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateItemDecisionRequest")


@_attrs_define
class UpdateItemDecisionRequest:
    """
    Attributes:
        decision (UpdateItemDecisionRequestDecision): Decision status Example: approved.
        comment (str | Unset): Comment for the decision (required when decision is 'change_requested') Example: Please
            update the introduction section.
        target_version (int | Unset): Target version for change request (only valid when decision is
            'change_requested'). If omitted, applies to latest version. Example: 1.
    """

    decision: UpdateItemDecisionRequestDecision
    comment: str | Unset = UNSET
    target_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        comment = self.comment

        target_version = self.target_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decision": decision,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if target_version is not UNSET:
            field_dict["targetVersion"] = target_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decision = UpdateItemDecisionRequestDecision(d.pop("decision"))

        comment = d.pop("comment", UNSET)

        target_version = d.pop("targetVersion", UNSET)

        update_item_decision_request = cls(
            decision=decision,
            comment=comment,
            target_version=target_version,
        )

        update_item_decision_request.additional_properties = d
        return update_item_decision_request

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
