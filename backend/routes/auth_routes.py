from fastapi import APIRouter
from models.users_model import UsersModel
from schemas.user_schema import UserSchema


router = APIRouter()


@router.post("/signup")
def signup(user: UserSchema):

    user_data = user.dict()

    existing_user = UsersModel.get_user_by_email(user.email)

    if existing_user:
        return {
            "message": "User already exists"
        }

    UsersModel.create_user(user_data)

    return {
        "message": "User created successfully"
    }

@router.post("/login")
def login(user: UserSchema):

    existing_user = UsersModel.get_user_by_email(user.email)

    if not existing_user:
        return {
            "message": "User not found"
        }

    if existing_user["password"] != user.password:
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Login successful",
        "user": {
            "name": existing_user["name"],
            "email": existing_user["email"]
        }
    }