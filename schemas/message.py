from pydantic import BaseModel


class Message(BaseModel):
    user_id: int
    chat_id: int
    text: str
