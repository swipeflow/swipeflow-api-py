from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery_method import DeliveryMethod
from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_data import NotificationData


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        id (str | Unset): Notification ID Example: 507f1f77bcf86cd799439011.
        user_id (str | Unset): User ID Example: 507f1f77bcf86cd799439012.
        type_ (NotificationType | Unset): Type of notification Example: ITEM_CREATED.
        title (str | Unset): Notification title Example: New Item Created.
        body (str | Unset): Notification body Example: John Doe created a new item.
        data (NotificationData | Unset): Additional notification data Example: {'itemId': '507f1f77bcf86cd799439012',
            'projectId': '507f1f77bcf86cd799439013'}.
        read (bool | Unset): Whether notification has been read Example: False.
        read_at (datetime.datetime | Unset): When notification was read Example: 2024-01-15T10:30:00Z.
        delivered_via (list[DeliveryMethod] | Unset): Delivery methods used Example: ['PUSH'].
        created_at (datetime.datetime | Unset): Creation timestamp Example: 2024-01-15T10:30:00Z.
    """

    id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    type_: NotificationType | Unset = UNSET
    title: str | Unset = UNSET
    body: str | Unset = UNSET
    data: NotificationData | Unset = UNSET
    read: bool | Unset = UNSET
    read_at: datetime.datetime | Unset = UNSET
    delivered_via: list[DeliveryMethod] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        title = self.title

        body = self.body

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        read = self.read

        read_at: str | Unset = UNSET
        if not isinstance(self.read_at, Unset):
            read_at = self.read_at.isoformat()

        delivered_via: list[str] | Unset = UNSET
        if not isinstance(self.delivered_via, Unset):
            delivered_via = []
            for delivered_via_item_data in self.delivered_via:
                delivered_via_item = delivered_via_item_data.value
                delivered_via.append(delivered_via_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if data is not UNSET:
            field_dict["data"] = data
        if read is not UNSET:
            field_dict["read"] = read
        if read_at is not UNSET:
            field_dict["readAt"] = read_at
        if delivered_via is not UNSET:
            field_dict["deliveredVia"] = delivered_via
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_data import NotificationData  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NotificationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NotificationType(_type_)

        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        _data = d.pop("data", UNSET)
        data: NotificationData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NotificationData.from_dict(_data)

        read = d.pop("read", UNSET)

        _read_at = d.pop("readAt", UNSET)
        read_at: datetime.datetime | Unset
        if isinstance(_read_at, Unset):
            read_at = UNSET
        else:
            read_at = datetime.datetime.fromisoformat(_read_at)

        _delivered_via = d.pop("deliveredVia", UNSET)
        delivered_via: list[DeliveryMethod] | Unset = UNSET
        if _delivered_via is not UNSET:
            delivered_via = []
            for delivered_via_item_data in _delivered_via:
                delivered_via_item = DeliveryMethod(delivered_via_item_data)

                delivered_via.append(delivered_via_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        notification = cls(
            id=id,
            user_id=user_id,
            type_=type_,
            title=title,
            body=body,
            data=data,
            read=read,
            read_at=read_at,
            delivered_via=delivered_via,
            created_at=created_at,
        )

        notification.additional_properties = d
        return notification

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
