from fastapi import APIRouter, Body, HTTPException, status, Request,Depends
from database.connection import get_session
from models.events import Event, EventUpdate
from sqlmodel import select

event_router = APIRouter(
    tags=["Events"]
)

events = []

@event_router.post("/new")
async def create_event(new_event: Event = Body(...),session = Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": "Event created successfully"
    }

@event_router.get("/", response_model=list[Event])
async def retrieve_all_events(session = Depends(get_session)) -> list[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int,session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.put("edit/{id}", response_model=Event)
async def retrieve_event(id: int,new_event_data: EventUpdate = Body(...),session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_event_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )



@event_router.delete("/{id}")
async def delete_event(id: int,session = Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        
        return {
            "message": "Event deleted successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
