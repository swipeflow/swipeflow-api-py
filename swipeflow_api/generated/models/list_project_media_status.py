from enum import StrEnum


class ListProjectMediaStatus(StrEnum):
    DELETED = "deleted"
    DELETE_PENDING = "delete_pending"
    IMPORT_PENDING = "import_pending"
    UPLOADED = "uploaded"
    UPLOAD_PENDING = "upload_pending"

    def __str__(self) -> str:
        return str(self.value)
