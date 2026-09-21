from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event import WebhookEvent
from ..models.webhook_type import WebhookType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """
    Attributes:
        id (str | Unset): Webhook ID Example: 507f1f77bcf86cd799439011.
        project_id (str | Unset): Project ID Example: 507f1f77bcf86cd799439012.
        name (str | Unset): Webhook name Example: My Webhook.
        url (str | Unset): Webhook URL Example: https://example.com/webhook.
        type_ (WebhookType | Unset): Webhook type Example: user.
        integration_provider (str | Unset): Integration provider name Example: zapier.
        integration_link (str | Unset): Link to integration setup Example: https://zapier.com/apps/myapp.
        events (list[WebhookEvent] | Unset): Events that trigger this webhook Example: ['item.created',
            'item.approved'].
        active (bool | Unset): Whether the webhook is active Example: True.
        trigger_count (int | Unset): Number of times webhook has been triggered Example: 42.
        created_at (datetime.datetime | Unset): Creation timestamp Example: 2024-01-01T00:00:00Z.
        updated_at (datetime.datetime | Unset): Last update timestamp Example: 2024-01-15T10:30:00Z.
    """

    id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    type_: WebhookType | Unset = UNSET
    integration_provider: str | Unset = UNSET
    integration_link: str | Unset = UNSET
    events: list[WebhookEvent] | Unset = UNSET
    active: bool | Unset = UNSET
    trigger_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        project_id = self.project_id

        name = self.name

        url = self.url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        integration_provider = self.integration_provider

        integration_link = self.integration_link

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        active = self.active

        trigger_count = self.trigger_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if integration_provider is not UNSET:
            field_dict["integrationProvider"] = integration_provider
        if integration_link is not UNSET:
            field_dict["integrationLink"] = integration_link
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if trigger_count is not UNSET:
            field_dict["triggerCount"] = trigger_count
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        project_id = d.pop("projectId", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: WebhookType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WebhookType(_type_)

        integration_provider = d.pop("integrationProvider", UNSET)

        integration_link = d.pop("integrationLink", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebhookEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookEvent(events_item_data)

                events.append(events_item)

        active = d.pop("active", UNSET)

        trigger_count = d.pop("triggerCount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        webhook = cls(
            id=id,
            project_id=project_id,
            name=name,
            url=url,
            type_=type_,
            integration_provider=integration_provider,
            integration_link=integration_link,
            events=events,
            active=active,
            trigger_count=trigger_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhook.additional_properties = d
        return webhook

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
