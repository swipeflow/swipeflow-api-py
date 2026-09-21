from enum import StrEnum


class AuditEventTargetType(StrEnum):
    API_KEY = "api_key"
    COMMENT = "comment"
    ITEM = "item"
    ITEM_VERSION = "item_version"
    MEMBER = "member"
    PROJECT = "project"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
