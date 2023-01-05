from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    chat_id: int
    send_from: str
    send_to: str
    text: str


class MessageInDB(Message):
    id: int
    created_date: datetime
