import pytest
from unittest.mock import MagicMock
from services.user_service import UserService
from schema.user_schema import UserCreate
from exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    UserNotFoundException
)

# ---------- CREATE USER ----------

def test_create_user_ok():
    service = UserService()
    db = MagicMock()

    service.repository.find_by_username = MagicMock(return_value=None)
    service.repository.save = MagicMock(return_value={"username": "rene"})

    data = UserCreate(
        username="rene",
        email="rene@test.com",
        first_name="Rene",
        last_name="Alarcon",
        role="USER"
    )

    user = service.create_user(db, data)

    assert user["username"] == "rene"


def test_create_user_already_exists():
    service = UserService()
    db = MagicMock()

    service.repository.find_by_username = MagicMock(return_value=True)

    data = UserCreate(
        username="rene",
        email="rene@test.com",
        first_name="Rene",
        last_name="Alarcon",
        role="USER"
    )

    with pytest.raises(UserAlreadyExistsException):
        service.create_user(db, data)

# ---------- GET USERS ----------

def test_get_all_users():
    service = UserService()
    db = MagicMock()

    service.repository.find_all = MagicMock(return_value=[])

    users = service.get_all_users(db)

    assert users == []


def test_get_user_by_id_ok():
    service = UserService()
    db = MagicMock()

    service.repository.find_by_id = MagicMock(return_value={"id": 1})

    user = service.get_user_by_id(db, 1)

    assert user["id"] == 1


def test_get_user_by_id_not_found():
    service = UserService()
    db = MagicMock()

    service.repository.find_by_id = MagicMock(return_value=None)

    with pytest.raises(UserNotFoundException):
        service.get_user_by_id(db, 99)
