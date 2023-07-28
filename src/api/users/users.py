import logging

import requests
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from src.api.users import schemas

from src.db.users import crud
from src.dependencies import get_db

router = APIRouter()
logger = logging.getLogger('api')


@router.post("/users", response_model=list[schemas.User])
def create_users(db: Session = Depends(get_db)):
    users = requests.get("https://reqres.in/api/users").json().get("data")

    all_registered = True
    for user in users:
        db_user = crud.get_user_by_id(db, user["id"])
        if not db_user:
            crud.create_user(db, user=schemas.User(**user))
            all_registered = False

    if all_registered:
        raise HTTPException(
                status_code=400, detail="All users already registered"
            )

    return users


@router.get("/user/{id}", response_model=schemas.User)
def read_user_by_id(id: int):
    user = requests.get(f"https://reqres.in/api/users/{id}").json().get("data")
    if user:
        user = schemas.User(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/user/{id}", response_model=schemas.User)
def delete_note(id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user = crud.delete_user(db, id)

    return user
