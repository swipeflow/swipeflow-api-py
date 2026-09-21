from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookRequest")


@_attrs_define
class CreateWebhookRequest:
    """
    Attributes:
        url (str): Webhook URL Example: https://example.com/webhook.
        events (list[WebhookEvent]): Events to trigger the webhook Example: ['item.created', 'item.approved'].
        name (str | Unset): Webhook name Example: My Webhook.
        secret (str | Unset): Secret for webhook signature Example: my_secret_key.
    """

    url: str
    events: list[WebhookEvent]
    name: str | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        name = self.name

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "events": events,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebhookEvent(events_item_data)

            events.append(events_item)

        name = d.pop("name", UNSET)

        secret = d.pop("secret", UNSET)

        create_webhook_request = cls(
            url=url,
            events=events,
            name=name,
            secret=secret,
        )

        create_webhook_request.additional_properties = d
        return create_webhook_request

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
