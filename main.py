from fastapi import FastAPI
from api.controllers.user_controller import router as user_router
from db.database import Base, engine
from exceptions.exception_handler import (
    user_not_found_handler,
    user_exists_handler
)
from exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)
import logging
from api.health import router as health_router



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("user-api")

app = FastAPI(
    title="API Gestión de Usuarios",
    description="API REST para la gestión de usuarios",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(user_router)



app.add_exception_handler(UserNotFoundException, user_not_found_handler)
app.add_exception_handler(UserAlreadyExistsException, user_exists_handler)
