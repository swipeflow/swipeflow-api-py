from enum import StrEnum


class ItemStatus(StrEnum):
    APPROVED = "approved"
    CHANGE_REQUESTED = "change_requested"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
