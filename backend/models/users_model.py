from pymongo.errors import DuplicateKeyError
from database.mongodb import db

users_collection = db["users"]

# Create unique index once
users_collection.create_index("email", unique=True)


class UsersModel:

    @staticmethod
    def create_user(user_data: dict):
        try:
            result = users_collection.insert_one(user_data)
            return {
                "success": True,
                "inserted_id": str(result.inserted_id)
            }

        except DuplicateKeyError:
            return {
                "success": False,
                "message": "User already exists"
            }

    @staticmethod
    def get_user_by_email(email: str):
        return users_collection.find_one({"email": email})

    @staticmethod
    def get_user_by_id(user_id: str):
        return users_collection.find_one({"_id": user_id})

    @staticmethod
    def update_user(user_id: str, updated_data: dict):
        return users_collection.update_one(
            {"_id": user_id},
            {"$set": updated_data}
        )

    @staticmethod
    def delete_user(user_id: str):
        return users_collection.delete_one({"_id": user_id})