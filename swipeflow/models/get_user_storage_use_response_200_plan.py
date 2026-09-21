from enum import StrEnum


class GetUserStorageUseResponse200Plan(StrEnum):
    FREE = "free"
    PRO = "pro"

    def __str__(self) -> str:
        return str(self.value)
