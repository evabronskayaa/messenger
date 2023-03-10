from fastapi import FastAPI
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8080,
        reload=True
    )
