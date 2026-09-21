from enum import StrEnum


class DecisionType(StrEnum):
    APPROVED = "approved"
    CHANGE_REQUESTED = "change_requested"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
