from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from omega.events.schemas import EventIn, EventOut
from omega.db.deps import get_db
from omega.db.models import Event

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=EventOut)
async def ingest_event(
        event: EventIn,
        db: AsyncSession = Depends(get_db),
):
    db_event = Event(
        source=event.source.value,
        event_type=event.event_type.value,
        actor=event.actor,
        target=event.target,
        ip_address=event.ip_address,
        event_data=event.metadata,
    )

    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)

    return db_event