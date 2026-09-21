from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_trigger_payload import RunTriggerPayload
    from ..models.run_trigger_trigger import RunTriggerTrigger


T = TypeVar("T", bound="RunTrigger")


@_attrs_define
class RunTrigger:
    """
    Attributes:
        message (str | Unset): Result message Example: Trigger executed successfully.
        trigger (RunTriggerTrigger | Unset):
        payload (RunTriggerPayload | Unset): Payload delivered to the webhook
        executed_at (datetime.datetime | Unset): Trigger execution timestamp Example: 2024-03-20T09:15:00Z.
    """

    message: str | Unset = UNSET
    trigger: RunTriggerTrigger | Unset = UNSET
    payload: RunTriggerPayload | Unset = UNSET
    executed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        trigger: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.to_dict()

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        executed_at: str | Unset = UNSET
        if not isinstance(self.executed_at, Unset):
            executed_at = self.executed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if payload is not UNSET:
            field_dict["payload"] = payload
        if executed_at is not UNSET:
            field_dict["executedAt"] = executed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_trigger_payload import RunTriggerPayload  # noqa: PLC0415
        from ..models.run_trigger_trigger import RunTriggerTrigger  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: RunTriggerTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = RunTriggerTrigger.from_dict(_trigger)

        _payload = d.pop("payload", UNSET)
        payload: RunTriggerPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = RunTriggerPayload.from_dict(_payload)

        _executed_at = d.pop("executedAt", UNSET)
        executed_at: datetime.datetime | Unset
        if isinstance(_executed_at, Unset):
            executed_at = UNSET
        else:
            executed_at = datetime.datetime.fromisoformat(_executed_at)

        run_trigger = cls(
            message=message,
            trigger=trigger,
            payload=payload,
            executed_at=executed_at,
        )

        run_trigger.additional_properties = d
        return run_trigger

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
