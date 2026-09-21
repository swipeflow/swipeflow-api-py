from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_status import ItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_decision import ItemDecision


T = TypeVar("T", bound="ItemStatusSnapshot")


@_attrs_define
class ItemStatusSnapshot:
    """Slim status projection of an item — status, version, and the latest decision only, without content or metadata. The
    cheap alternative to fetching the full item when polling.

        Attributes:
            id (str | Unset): Item ID Example: 507f1f77bcf86cd799439011.
            status (ItemStatus | Unset): Status of an item in the approval workflow Example: pending.
            version (int | Unset): Version number Example: 1.
            decision (ItemDecision | None | Unset): The most recent decision, or null if none has been made yet
    """

    id: str | Unset = UNSET
    status: ItemStatus | Unset = UNSET
    version: int | Unset = UNSET
    decision: ItemDecision | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.item_decision import ItemDecision  # noqa: PLC0415

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        version = self.version

        decision: dict[str, Any] | None | Unset
        if isinstance(self.decision, Unset):
            decision = UNSET
        elif isinstance(self.decision, ItemDecision):
            decision = self.decision.to_dict()
        else:
            decision = self.decision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_decision import ItemDecision  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: ItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ItemStatus(_status)

        version = d.pop("version", UNSET)

        def _parse_decision(data: object) -> ItemDecision | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                decision_type_1 = ItemDecision.from_dict(data)

                return decision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ItemDecision | None | Unset, data)

        decision = _parse_decision(d.pop("decision", UNSET))

        item_status_snapshot = cls(
            id=id,
            status=status,
            version=version,
            decision=decision,
        )

        item_status_snapshot.additional_properties = d
        return item_status_snapshot

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
