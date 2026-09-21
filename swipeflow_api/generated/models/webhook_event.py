from enum import StrEnum


class WebhookEvent(StrEnum):
    ITEM_APPROVED = "item.approved"
    ITEM_CHANGE_REQUESTED = "item.change_requested"
    ITEM_CREATED = "item.created"
    ITEM_DELETED = "item.deleted"
    ITEM_PROCESSED = "item.processed"
    ITEM_REJECTED = "item.rejected"
    ITEM_UPDATED = "item.updated"
    PROJECT_TRIGGER = "project.trigger"

    def __str__(self) -> str:
        return str(self.value)
