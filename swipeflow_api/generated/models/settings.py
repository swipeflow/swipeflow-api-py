from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_settings import MediaSettings
    from ..models.notification_preference import NotificationPreference


T = TypeVar("T", bound="Settings")


@_attrs_define
class Settings:
    """
    Attributes:
        theme (str | Unset): UI theme Example: dark.
        auto_dark_mode (bool | Unset): Automatically switch to dark mode based on system preference Example: True.
        media_settings (MediaSettings | Unset):
        notification_preferences (list[NotificationPreference] | Unset):
        notify_self_actions (bool | Unset): Whether to notify the user about actions they themselves performed (excludes
            API key, OAuth and MCP activity, which always notifies). Defaults to false. Example: False.
        auto_grid_landscape (bool | Unset): Whether the item queue auto-switches to grid view in landscape orientation
            (mobile/tablet) or on desktop-sized screens Example: True.
    """

    theme: str | Unset = UNSET
    auto_dark_mode: bool | Unset = UNSET
    media_settings: MediaSettings | Unset = UNSET
    notification_preferences: list[NotificationPreference] | Unset = UNSET
    notify_self_actions: bool | Unset = UNSET
    auto_grid_landscape: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        theme = self.theme

        auto_dark_mode = self.auto_dark_mode

        media_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media_settings, Unset):
            media_settings = self.media_settings.to_dict()

        notification_preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_preferences, Unset):
            notification_preferences = []
            for notification_preferences_item_data in self.notification_preferences:
                notification_preferences_item = (
                    notification_preferences_item_data.to_dict()
                )
                notification_preferences.append(notification_preferences_item)

        notify_self_actions = self.notify_self_actions

        auto_grid_landscape = self.auto_grid_landscape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if theme is not UNSET:
            field_dict["theme"] = theme
        if auto_dark_mode is not UNSET:
            field_dict["autoDarkMode"] = auto_dark_mode
        if media_settings is not UNSET:
            field_dict["mediaSettings"] = media_settings
        if notification_preferences is not UNSET:
            field_dict["notificationPreferences"] = notification_preferences
        if notify_self_actions is not UNSET:
            field_dict["notifySelfActions"] = notify_self_actions
        if auto_grid_landscape is not UNSET:
            field_dict["autoGridLandscape"] = auto_grid_landscape

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_settings import MediaSettings  # noqa: PLC0415
        from ..models.notification_preference import (
            NotificationPreference,  # noqa: PLC0415
        )

        d = dict(src_dict)
        theme = d.pop("theme", UNSET)

        auto_dark_mode = d.pop("autoDarkMode", UNSET)

        _media_settings = d.pop("mediaSettings", UNSET)
        media_settings: MediaSettings | Unset
        if isinstance(_media_settings, Unset):
            media_settings = UNSET
        else:
            media_settings = MediaSettings.from_dict(_media_settings)

        _notification_preferences = d.pop("notificationPreferences", UNSET)
        notification_preferences: list[NotificationPreference] | Unset = UNSET
        if _notification_preferences is not UNSET:
            notification_preferences = []
            for notification_preferences_item_data in _notification_preferences:
                notification_preferences_item = NotificationPreference.from_dict(
                    notification_preferences_item_data
                )

                notification_preferences.append(notification_preferences_item)

        notify_self_actions = d.pop("notifySelfActions", UNSET)

        auto_grid_landscape = d.pop("autoGridLandscape", UNSET)

        settings = cls(
            theme=theme,
            auto_dark_mode=auto_dark_mode,
            media_settings=media_settings,
            notification_preferences=notification_preferences,
            notify_self_actions=notify_self_actions,
            auto_grid_landscape=auto_grid_landscape,
        )

        settings.additional_properties = d
        return settings

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
