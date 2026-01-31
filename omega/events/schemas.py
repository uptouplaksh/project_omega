from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class EventSource(str, Enum):
    system = "system"
    application = "application"
    network = "network"


class EventType(str, Enum):
    auth_success = "auth_success"
    auth_failure = "auth_failure"
    privilege_attempt = "privilege_attempt"
    config_change = "config_change"
    generic = "generic"


class EventIn(BaseModel):
    source: EventSource
    event_type: EventType

    actor: str | None = None
    target: str | None = None
    ip_address: str | None = None

    metadata: dict = Field(default_factory=dict)


class EventOut(BaseModel):
    id: int
    timestamp: datetime
