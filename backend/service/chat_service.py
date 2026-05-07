import os
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
from config.database import chat_collection
from config.system_prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

MODEL_NAME = os.getenv("OPENROUTER_MODEL")


def get_chat_history(username):
    history = list(
        chat_collection.find(
            {"username": username},
            {"_id": 0}
        )
        .sort("timestamp", -1)
        .limit(20)
    )

    history.reverse()

    return [
        {
            "role": msg["role"],
            "content": msg["message"]
        }
        for msg in history
    ]


def save_chat_message(username, role, message):
    chat_collection.insert_one({
        "username": username,
        "role": role,
        "message": message,
        "timestamp": datetime.utcnow()
    })


def generate_ai_response(username, prompt):
    history = get_chat_history(username)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )

    ai_response = response.choices[0].message.content

    save_chat_message(username, "user", prompt)
    save_chat_message(username, "assistant", ai_response)

    return ai_response