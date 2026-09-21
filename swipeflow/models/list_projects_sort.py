from enum import StrEnum


class ListProjectsSort(StrEnum):
    CREATEDAT = "createdAt"
    NAME = "name"
    PENDINGITEMS = "pendingItems"
    TOTALITEMS = "totalItems"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
