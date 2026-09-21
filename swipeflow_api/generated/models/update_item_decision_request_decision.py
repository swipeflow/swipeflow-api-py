from enum import StrEnum


class UpdateItemDecisionRequestDecision(StrEnum):
    APPROVED = "approved"
    CHANGE_REQUESTED = "change_requested"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
