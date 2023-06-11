from fastapi import APIRouter, Depends, HTTPException, status

from crud.user import get_user_by_id as crud_get_user_by_id, \
    get_users as crud_get_users, create_user as crud_create_user, change_name as crud_change_name, delete_user_by_id
from deps import get_current_user

from schemas.user import User


router = APIRouter(prefix="/user")


@router.get("/list")
async def get_users():
    users = crud_get_users()
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return users


@router.get("/get/{user_id}")
async def get_user_by_id(user_id: int = Depends(get_current_user)):
    user_id = crud_get_user_by_id(user_id)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user_id


@router.post("/new", response_model=User)
async def create_user(user: User):
    return crud_create_user(user)


@router.put("/change_name/{user_id}")
async def change_name(new_name: str, user_id: int = Depends(get_current_user)):
    return crud_change_name(user_id, new_name)


@router.delete("/delete/{user_id}", response_model=User)
async def delete_user(user_id: int = Depends(get_current_user)):
    user_id = delete_user_by_id(user_id)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user_id
