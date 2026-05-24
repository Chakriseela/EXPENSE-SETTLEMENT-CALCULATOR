from pydantic import BaseModel
from typing import List


class FrequentSpentOn(BaseModel):
    item: str
    count: int

class FrequentAmount(BaseModel):
    amount: int
    count: int

class Member(BaseModel):
    _id: str
    name: str
    transactionFrequency: int
    frequentSpentOns: List[FrequentSpentOn]
    frequentAmounts: List[FrequentAmount]
    amountTheySpentOnMe: int
    amountISpentOnThem: int
    netBalance: int
    balanceStatus: str


class Transaction(BaseModel):
    _id: str
    personId: str
    amount: int
    type: str
    category: str
    spentOn: str
    dateTime: str



class Profile(BaseModel):
    userName: str
    email: str
    createdAt: str

class UserExpenseDetails(BaseModel):
    _id: str
    profile: Profile
    members: List[Member]
    transactions: List[Transaction]

class UsersExpenseDetails(BaseModel):
    users_details: List[UserExpenseDetails]