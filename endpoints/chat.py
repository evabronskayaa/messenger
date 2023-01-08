import datetime

from fastapi import APIRouter

from crud.chat import chat_database, user_chat_database
from crud.message import message_database
from schemas.chat import Chat, ChatInDB
from schemas.message import MessageInDB

router = APIRouter(prefix="/chat")


@router.get("/{chat_id}")
async def get_chat(chat_id: int):
    chat_users = list()
    for user in user_chat_database:
        for param, value in user.items():
            if param == "chat_id" and value == chat_id:
                chat_users.append(user)
    return chat_database[chat_id - 1], chat_users


@router.post("/", response_model=ChatInDB)
async def create_chat(chat: Chat):
    chat_db = ChatInDB(name=chat.name, type=chat.type, created_date=chat.created_date)
    return chat_db


@router.put("/{chat_id}", response_model=ChatInDB)
async def update_chat(chat_id: int, chat: Chat):
    chat_db = chat_database[chat_id - 1]
    for param, value in chat.dict().items():
        chat_db[param] = value
    return chat_db


@router.delete("/{chat_id}")
async def delete_chat(chat_id: int):
    db = list(chat_database)
    del db[chat_id - 1]


@router.get("/{chat_id}/messages", response_model=list[MessageInDB])
async def get_last_messages(chat_id: int):
    message_db = []
    for message in message_database:
        for param, value in message.items():
            if param == "chat_id" and value == chat_id:
                message_db.append(message)
    return message_db[-5:]


@router.get("/active", response_model=list[ChatInDB])
async def get_active_chats():
    pass
