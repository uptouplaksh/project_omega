from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    JSON,
    Text
)

from omega.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )
    source = Column(String, index=True)
    event_type = Column(String, index=True)

    actor = Column(String, nullable=True)
    target = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    event_data = Column(JSON, default=dict)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    severity = Column(String, index=True)
    status = Column(String, default="open", index=True)

    summary = Column(Text)
