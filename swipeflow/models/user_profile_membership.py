from enum import StrEnum


class UserProfileMembership(StrEnum):
    FREE = "free"
    PRO = "pro"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
