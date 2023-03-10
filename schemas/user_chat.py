from pydantic import BaseModel


class UserChat(BaseModel):
    user_id: int
    chat_id: int


class UserChatInDB(UserChat):
    id: int

    class Config:
        orm_mode = True
