# tests/helpers/user_factory.py
from models.user_model import User

def create_user(**overrides):
    """
    Crea un usuario válido para tests.
    Se pueden sobreescribir campos según el test.
    """
    data = {
        "username": "rene",
        "email": "rene@test.com",
        "first_name": "Rene",
        "last_name": "Alarcon",
        "role": "user",
        "active": True,
    }

    data.update(overrides)
    return User(**data)
