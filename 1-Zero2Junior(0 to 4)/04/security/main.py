from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.users import user_router
from routes.events import event_router
from database.connection import Settings # new


app = FastAPI()

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


settings = Settings()

@app.on_event("startup")
async def on_startup():
    await settings.initialize_database()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")



