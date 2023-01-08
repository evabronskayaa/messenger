from fastapi import APIRouter, Depends, HTTPException, status

from deps import get_db
import crud.user as crud
from schemas.user import User, UserInDB


router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user(user_id: int, db=Depends(get_db)):
    user = crud.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user


@router.post("/", response_model=UserInDB)
async def create_user(user: User, db=Depends(get_db)):
    result = crud.create_user(db=db, user=user)
    return result


@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user: User, db=Depends(get_db)):
    user_db = crud.update_user(db=db, user_id=user_id, user=user)
    return user_db


@router.delete("/{user_id}")
async def delete_user(user_id: int, db=Depends(get_db)):
    crud.delete_user(db=db, user_id=user_id)
