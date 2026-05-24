# users_expense_details_model.py
from bson import ObjectId
from database.mongodb import db


users_expense_collection = db["users_expense_details"]

class UsersExpenseDetailsModel:

    @staticmethod
    def update_user_expense_details(
        user_id: str,
        operation: str,
        data: dict
    ):
        """
        operation examples:
        "$set", "$push", "$pull"
        """

        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {
                operation: data
            }
        )



    @staticmethod
    def create_user_expense_details(data: dict):
        return users_expense_collection.insert_one(data)

    @staticmethod
    def get_user_expense_details(user_id: str):
        return users_expense_collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def update_user_expense_details(user_id: str, updated_data: dict):
        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": updated_data}
        )

    @staticmethod
    def delete_user_expense_details(user_id: str):
        return users_expense_collection.delete_one({"_id": ObjectId(user_id)})

    @staticmethod
    def add_transaction(user_id: str, transaction_data: dict):
        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"transactions": transaction_data}}
        )

    @staticmethod
    def delete_transaction(user_id: str, transaction_id: str):
        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$pull": {
                    "transactions": {
                        "_id": transaction_id
                    }
                }
            }
        )

    @staticmethod
    def add_member(user_id: str, member_data: dict):
        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"members": member_data}}
        )

    @staticmethod
    def delete_member(user_id: str, member_id: str):
        return users_expense_collection.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$pull": {
                    "members": {
                        "_id": member_id
                    }
                }
            }
        )