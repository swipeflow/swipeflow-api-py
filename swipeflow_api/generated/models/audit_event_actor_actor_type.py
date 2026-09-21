from enum import StrEnum


class AuditEventActorActorType(StrEnum):
    API_KEY = "api_key"
    OAUTH_CLIENT = "oauth_client"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
