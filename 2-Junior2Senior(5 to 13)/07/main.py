from fastapi import FastAPI, Depends

from api import (
    recipes,
    users,
    posts,
    login,
    admin,
    keywords,
    admin_mcontainer,
    complaints,
)
from dependencies.global_transactions import log_transaction

app = FastAPI(dependencies=[Depends(log_transaction)])

app.include_router(recipes.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(posts.router, prefix="/api/v1")
app.include_router(login.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")
app.include_router(keywords.router, prefix="/api/v1")
app.include_router(admin_mcontainer.router, prefix="/api/v1")
app.include_router(complaints.router, prefix="/api/v1")


@app.get("/")
def index():
    return {"message": "Cooking Recipe Rating Prototype!"}
