from fastapi import APIRouter, Body, HTTPException, status,Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from database.connection import Database
from beanie import PydanticObjectId
from models.users import User, UserSignIn,TokenResponse
from auth.hash_password import HashPassword

hash_password = HashPassword()
user_router = APIRouter(
    tags=["User"],
)

user_database = Database(User)


@user_router.post("/signup")
async def sign_user_up(user: User = Body(...)) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with email provided exists already.'
        )

    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)

    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if hash_password.verify_hash(user.password,user_exist.password):
        access_token = create_access_token(user_exist.email)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Wrong credentials passed"
    )
    
