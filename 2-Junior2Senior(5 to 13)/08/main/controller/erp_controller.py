from fastapi import APIRouter

router = APIRouter()


@router.get("/erp/{portal_id}")
def access_portal(portal_id: int):
    return {"message": "Wrong ID"}
