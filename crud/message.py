from datetime import datetime

message_database = [
    {
        "id": 1,
        "chat_id": 1,
        "send_from": "user_1",
        "send_to": "user_2",
        "created_date": datetime(2022, 1, 6, 19, 39, 1),
        "text": "Hey!"
    },
    {
        "id": 2,
        "chat_id": 1,
        "send_from": "user_2",
        "send_to": "user_1",
        "created_date": datetime(2022, 1, 6, 19, 39, 2),
        "text": "Wow"
    },
]
