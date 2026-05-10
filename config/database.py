import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = "mongodb://nandini:VODM0juaCdkR7aYfOGYSCKt2ImUJwY_ojDdj7-kxTPEUPg-v@db3be873-5280-44f4-9db3-df4fc090bdfa.asia-south2.firestore.goog:443/default?loadBalanced=true&tls=true&authMechanism=SCRAM-SHA-256&retryWrites=false"

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client.get_default_database()

chat_collection = db["chat_history"]

print("MongoDB Connected Successfully")