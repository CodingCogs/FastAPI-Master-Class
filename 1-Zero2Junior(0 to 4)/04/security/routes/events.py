from fastapi import APIRouter, Body, HTTPException, status, Request,Depends
from database.connection import Database
from models.events import Event, EventUpdate
from beanie import PydanticObjectId

event_router = APIRouter(
    tags=["Events"]
)

event_database = Database(Event)

@event_router.post("/new")
async def create_event(new_event: Event = Body(...)) -> dict:
    await event_database.save(new_event)
    return {
        "message": "Event created successfully"
    }

@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId,) -> Event:
    event = await event_database.get(id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.put("/edit/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId,new_event_data: EventUpdate = Body(...)) -> Event:
    event = await event_database.update(id,new_event_data)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )



@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId,) -> dict:
    event = await event_database.delete(id)
    if event:
        
        return {
            "message": "Event deleted successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
