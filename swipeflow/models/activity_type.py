from enum import StrEnum


class ActivityType(StrEnum):
    APPROVED = "approved"
    CHANGE_REQUESTED = "change_requested"
    COMMENTED = "commented"
    CREATED = "created"
    DELETED = "deleted"
    REJECTED = "rejected"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
