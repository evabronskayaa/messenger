from fastapi import FastAPI

from endpoints.user import router as user_router
from endpoints.chat import router as chat_router
from endpoints.message import router as message_router

app = FastAPI()

app.include_router(user_router, tags=["user"])
app.include_router(chat_router, tags=["chat"])
app.include_router(message_router, tags=["message"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
