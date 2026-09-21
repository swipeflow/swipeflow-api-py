from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_log_payload import WebhookLogPayload


T = TypeVar("T", bound="WebhookLog")


@_attrs_define
class WebhookLog:
    """
    Attributes:
        id (str | Unset): Log ID Example: 507f1f77bcf86cd799439011.
        webhook_id (str | Unset): Webhook ID Example: 507f1f77bcf86cd799439012.
        event (str | Unset): Event that triggered the webhook Example: item.created.
        payload (WebhookLogPayload | Unset): Payload sent to webhook Example: {'itemId': '123', 'action': 'created'}.
        response_status (int | Unset): HTTP response status code Example: 200.
        response_body (str | Unset): Response body from webhook endpoint Example: {"success":true}.
        error (str | Unset): Error message if delivery failed Example: Connection timeout.
        timestamp (datetime.datetime | Unset): Delivery timestamp Example: 2024-01-15T10:30:00Z.
        latency (int | Unset): Request latency in milliseconds Example: 150.
    """

    id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    event: str | Unset = UNSET
    payload: WebhookLogPayload | Unset = UNSET
    response_status: int | Unset = UNSET
    response_body: str | Unset = UNSET
    error: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    latency: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        webhook_id = self.webhook_id

        event = self.event

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        response_status = self.response_status

        response_body = self.response_body

        error = self.error

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        latency = self.latency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if event is not UNSET:
            field_dict["event"] = event
        if payload is not UNSET:
            field_dict["payload"] = payload
        if response_status is not UNSET:
            field_dict["responseStatus"] = response_status
        if response_body is not UNSET:
            field_dict["responseBody"] = response_body
        if error is not UNSET:
            field_dict["error"] = error
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if latency is not UNSET:
            field_dict["latency"] = latency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_log_payload import WebhookLogPayload  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        event = d.pop("event", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: WebhookLogPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = WebhookLogPayload.from_dict(_payload)

        response_status = d.pop("responseStatus", UNSET)

        response_body = d.pop("responseBody", UNSET)

        error = d.pop("error", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        latency = d.pop("latency", UNSET)

        webhook_log = cls(
            id=id,
            webhook_id=webhook_id,
            event=event,
            payload=payload,
            response_status=response_status,
            response_body=response_body,
            error=error,
            timestamp=timestamp,
            latency=latency,
        )

        webhook_log.additional_properties = d
        return webhook_log

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
