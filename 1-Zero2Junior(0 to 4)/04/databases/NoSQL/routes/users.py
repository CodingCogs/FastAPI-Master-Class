from fastapi import APIRouter, Body, HTTPException, status
from database.connection import Database
from beanie import PydanticObjectId
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)

user_database = Database(User)


@user_router.post("/signup")
async def sign_user_up(data: User = Body(...)) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with email provided exists already.'
        )

    await user_database.save(user)

    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn = Body(...)) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if user_exist.password == user.password:
        return {
        "message": "User signed in successfully"
    }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Wrong credentials passed"
    )
    
