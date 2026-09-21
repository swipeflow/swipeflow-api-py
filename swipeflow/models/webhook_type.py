from enum import StrEnum


class WebhookType(StrEnum):
    DYNAMIC = "dynamic"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
