from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_bot_response
from database import chat_collection

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Backend working"}
class ChatRequest(BaseModel):
    user_id: str
    message: str

@app.post("/chat")

def chat(req: ChatRequest):

    previous_chats = list(
        chat_collection.find({"user_id": req.user_id})
    )

    bot_reply = get_bot_response(req.message)

    chat_collection.insert_one({
        "user_id": req.user_id,
        "user_message": req.message,
        "bot_reply": bot_reply
    })

    return {
        "reply": bot_reply
    }