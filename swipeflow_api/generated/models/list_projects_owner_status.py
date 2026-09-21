from enum import StrEnum


class ListProjectsOwnerStatus(StrEnum):
    ORPHANED = "orphaned"

    def __str__(self) -> str:
        return str(self.value)
