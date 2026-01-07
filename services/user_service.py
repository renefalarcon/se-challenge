from repository.user_repository import UserRepository
from models.user_model import User
from exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)
import logging

logger = logging.getLogger(__name__)

class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, db, data):
        logger.info(f"Usuario Creado {data.username}")

        if self.repository.find_by_username(db, data.username):
            logger.warning(f"Usuario existe: {data.username}")
            raise UserAlreadyExistsException()

        user = User(**data.dict())
        return self.repository.save(db, user)

    def get_all_users(self, db):
        return self.repository.find_all(db)

    def get_user_by_id(self, db, user_id: int):
        user = self.repository.find_by_id(db, user_id)
        if not user:
            raise UserNotFoundException()
        return user

    def update_user(self, db, user_id: int, data):
        user = self.get_user_by_id(db, user_id)

        for field, value in data.dict(exclude_unset=True).items():
            setattr(user, field, value)

        return self.repository.save(db, user)

    def delete_user(self, db, user_id: int):
        user = self.get_user_by_id(db, user_id)
        self.repository.delete(db, user)
