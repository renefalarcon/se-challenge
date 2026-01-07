from sqlalchemy.orm import Session
from models.user_model import User

class UserRepository:

    def find_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def find_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def find_all(self, db: Session):
        return db.query(User).all()

    def save(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user: User):
        db.delete(user)
        db.commit()
