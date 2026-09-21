from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookRequest")


@_attrs_define
class UpdateWebhookRequest:
    """
    Attributes:
        name (str | Unset): Webhook name Example: Updated Webhook Name.
        url (str | Unset): Webhook URL Example: https://example.com/new-webhook.
        events (list[WebhookEvent] | Unset): Events to trigger the webhook Example: ['item.created', 'item.approved'].
        active (bool | Unset): Whether the webhook is active Example: True.
        secret (str | Unset): Secret for webhook signature Example: new_secret_key.
    """

    name: str | Unset = UNSET
    url: str | Unset = UNSET
    events: list[WebhookEvent] | Unset = UNSET
    active: bool | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        active = self.active

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebhookEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookEvent(events_item_data)

                events.append(events_item)

        active = d.pop("active", UNSET)

        secret = d.pop("secret", UNSET)

        update_webhook_request = cls(
            name=name,
            url=url,
            events=events,
            active=active,
            secret=secret,
        )

        update_webhook_request.additional_properties = d
        return update_webhook_request

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
