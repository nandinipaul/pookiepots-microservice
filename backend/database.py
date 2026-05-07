from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

db = client["pookiepots"]

chat_collection = db["chats"]

print("MongoDB Connected")