from enum import StrEnum


class ContentType(StrEnum):
    AUDIO = "audio"
    HTML = "html"
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
