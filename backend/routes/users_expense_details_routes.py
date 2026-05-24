from fastapi import APIRouter, HTTPException
from models.users_expense_details_model import UsersExpenseDetailsModel

from schemas.user_details_schema import (
    UsersExpenseDetails,
    UserExpenseDetails,
    Transaction,
    Member
)

router = APIRouter()


# =========================
# GET USER EXPENSE DETAILS
# =========================
@router.get(
    "/user-expense-details/{user_id}",
    response_model=UserExpenseDetails
)
def get_user_expense_details(user_id: str):

    data = UsersExpenseDetailsModel.get_user_expense_details(user_id)

    if not data:
        raise HTTPException(status_code=404, detail="User not found")

    # convert ObjectId
    data["_id"] = str(data["_id"])

    return data


# =========================
# CREATE USER EXPENSE DETAILS
# =========================
@router.post(
    "/user-expense-details/{user_id}",
    response_model=dict
)
def create_user_expense_details(
    user_id: str,
    data: UserExpenseDetails
):

    payload = data.dict()
    payload["_id"] = user_id

    result = UsersExpenseDetailsModel.create_user_expense_details(payload)

    return {
        "success": True,
        "message": "Expense details created",
        "inserted_id": str(result.inserted_id)
    }


# =========================
# GENERIC UPDATE (SET / PUSH / PULL)
# =========================
@router.patch("/user-expense-details/{user_id}")
def update_user_expense_details(
    user_id: str,
    operation: str,
    data: dict
):

    result = UsersExpenseDetailsModel.update_user_expense_details(
        user_id=user_id,
        operation=operation,
        data=data
    )

    return {
        "success": True,
        "message": "Update successful",
        "matched_count": result.matched_count,
        "modified_count": result.modified_count
    }


# =========================
# DELETE USER EXPENSE DETAILS
# =========================
@router.delete("/user-expense-details/{user_id}")
def delete_user_expense_details(user_id: str):

    result = UsersExpenseDetailsModel.delete_user_expense_details(user_id)

    return {
        "success": True,
        "message": "User expense details deleted",
        "deleted_count": result.deleted_count
    }


# =========================
# ADD TRANSACTION (WITH SCHEMA)
# =========================
@router.post(
    "/user-expense-details/{user_id}/transaction",
    response_model=dict
)
def add_transaction(
    user_id: str,
    transaction_data: Transaction
):

    result = UsersExpenseDetailsModel.add_transaction(
        user_id=user_id,
        transaction_data=transaction_data.dict()
    )

    return {
        "success": True,
        "message": "Transaction added",
        "modified_count": result.modified_count
    }


# =========================
# DELETE TRANSACTION
# =========================
@router.delete("/user-expense-details/{user_id}/transaction/{transaction_id}")
def delete_transaction(user_id: str, transaction_id: str):

    result = UsersExpenseDetailsModel.delete_transaction(
        user_id=user_id,
        transaction_id=transaction_id
    )

    return {
        "success": True,
        "message": "Transaction deleted",
        "modified_count": result.modified_count
    }


# =========================
# ADD MEMBER (WITH SCHEMA)
# =========================
@router.post(
    "/user-expense-details/{user_id}/member",
    response_model=dict
)
def add_member(
    user_id: str,
    member_data: Member
):

    result = UsersExpenseDetailsModel.add_member(
        user_id=user_id,
        member_data=member_data.dict()
    )

    return {
        "success": True,
        "message": "Member added",
        "modified_count": result.modified_count
    }


# =========================
# DELETE MEMBER
# =========================
@router.delete("/user-expense-details/{user_id}/member/{member_id}")
def delete_member(user_id: str, member_id: str):

    result = UsersExpenseDetailsModel.delete_member(
        user_id=user_id,
        member_id=member_id
    )

    return {
        "success": True,
        "message": "Member deleted",
        "modified_count": result.modified_count
    }