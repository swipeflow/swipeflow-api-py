from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaSettings")


@_attrs_define
class MediaSettings:
    """
    Attributes:
        auto_play (bool | Unset): Auto-play media Example: True.
        loop_videos (bool | Unset): Loop videos Example: True.
        mute_player (bool | Unset): Mute player by default Example: False.
        show_controls (bool | Unset): Show media controls Example: True.
    """

    auto_play: bool | Unset = UNSET
    loop_videos: bool | Unset = UNSET
    mute_player: bool | Unset = UNSET
    show_controls: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_play = self.auto_play

        loop_videos = self.loop_videos

        mute_player = self.mute_player

        show_controls = self.show_controls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_play is not UNSET:
            field_dict["autoPlay"] = auto_play
        if loop_videos is not UNSET:
            field_dict["loopVideos"] = loop_videos
        if mute_player is not UNSET:
            field_dict["mutePlayer"] = mute_player
        if show_controls is not UNSET:
            field_dict["showControls"] = show_controls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_play = d.pop("autoPlay", UNSET)

        loop_videos = d.pop("loopVideos", UNSET)

        mute_player = d.pop("mutePlayer", UNSET)

        show_controls = d.pop("showControls", UNSET)

        media_settings = cls(
            auto_play=auto_play,
            loop_videos=loop_videos,
            mute_player=mute_player,
            show_controls=show_controls,
        )

        media_settings.additional_properties = d
        return media_settings

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
