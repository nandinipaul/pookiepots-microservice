from fastapi import APIRouter
from model.chat_model import ChatRequest
from service.chat_service import generate_ai_response
from config.database import chat_collection

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    response = generate_ai_response(
        request.username,
        request.prompt
    )

    return {
        "username": request.username,
        "response": response
    }


@router.get("/history/{username}")
def get_history(username: str):
    history = list(
        chat_collection.find(
            {"username": username},
            {"_id": 0}
        ).sort("timestamp", 1)
    )

    return {
        "username": username,
        "history": history
    }