from enum import StrEnum


class ProjectRole(StrEnum):
    ADMIN = "admin"
    EDITOR = "editor"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
