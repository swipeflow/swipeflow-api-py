from enum import StrEnum


class CreateMediaUploadResponse201UploadMethod(StrEnum):
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
