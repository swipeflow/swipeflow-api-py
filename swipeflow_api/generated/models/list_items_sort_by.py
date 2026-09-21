from enum import StrEnum


class ListItemsSortBy(StrEnum):
    CREATEDAT = "createdAt"
    STATUS = "status"
    TITLE = "title"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
