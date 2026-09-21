from enum import StrEnum


class NotificationPriority(StrEnum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    URGENT = "urgent"

    def __str__(self) -> str:
        return str(self.value)
