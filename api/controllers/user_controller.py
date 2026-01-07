from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.user_schema import UserCreate, UserUpdate, UserResponse
from services.user_service import UserService
from db.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@router.get("", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return service.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service.delete_user(db, user_id)
