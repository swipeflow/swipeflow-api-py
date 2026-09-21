from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_event_context_type_0_client_type import (
    AuditEventContextType0ClientType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditEventContextType0")


@_attrs_define
class AuditEventContextType0:
    """Request context. Included for the caller's own feed and the admin feed; on a project feed only for a platform admin
    or the project's OWNER/ADMIN.

        Attributes:
            ip (str | Unset):
            user_agent (str | Unset):
            request_id (str | Unset):
            client_type (AuditEventContextType0ClientType | Unset): Which surface the request came through.
    """

    ip: str | Unset = UNSET
    user_agent: str | Unset = UNSET
    request_id: str | Unset = UNSET
    client_type: AuditEventContextType0ClientType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        user_agent = self.user_agent

        request_id = self.request_id

        client_type: str | Unset = UNSET
        if not isinstance(self.client_type, Unset):
            client_type = self.client_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if client_type is not UNSET:
            field_dict["clientType"] = client_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        request_id = d.pop("requestId", UNSET)

        _client_type = d.pop("clientType", UNSET)
        client_type: AuditEventContextType0ClientType | Unset
        if isinstance(_client_type, Unset):
            client_type = UNSET
        else:
            client_type = AuditEventContextType0ClientType(_client_type)

        audit_event_context_type_0 = cls(
            ip=ip,
            user_agent=user_agent,
            request_id=request_id,
            client_type=client_type,
        )

        audit_event_context_type_0.additional_properties = d
        return audit_event_context_type_0

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
