from enum import StrEnum


class AuthProvider(StrEnum):
    APPLE = "apple"
    EMAIL = "email"
    GITHUB = "github"
    GOOGLE = "google"

    def __str__(self) -> str:
        return str(self.value)
