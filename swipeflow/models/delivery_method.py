from enum import StrEnum


class DeliveryMethod(StrEnum):
    EMAIL = "EMAIL"
    PUSH = "PUSH"

    def __str__(self) -> str:
        return str(self.value)
