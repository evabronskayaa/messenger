from datetime import datetime

from pydantic import BaseModel


class Chat(BaseModel):
    name: str
    type: str


class ChatInDB(Chat):
    id: int
    created_date: datetime
