import os
from dotenv import load_dotenv 
from pymongo import MongoClient
load_dotenv()

MONGO_URL = os.getenv("YOUR_MONGODB_URL")

client = MongoClient(MONGO_URL)

db = client["paytrack_db"]

users_collection = db["users"]

members_collection = db["members_details"]