from enum import StrEnum


class AuditEventContextType0ClientType(StrEnum):
    ANDROID = "android"
    API = "api"
    IOS = "ios"
    MCP = "mcp"
    OAUTH = "oauth"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
