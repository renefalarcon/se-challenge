from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status
from typing import List

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

@router.post("",
            summary="Crear usuario",
            description="Crea un nuevo usuario en el sistema",
            response_model=UserResponse,
            status_code=status.HTTP_200_OK,
            responses={
                200: {"description": "Usuario creado correctamente"},
                409: {"description": "El usuario ya existe"},
                422: {"description": "Datos inválidos"}
            })
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@router.get("",
            summary="Listar usuarios",
            description="Obtiene la lista de todos los usuarios",
            response_model= List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return service.get_all_users(db)

@router.get("/{user_id}",
            summary="Obtener usuario por ID",
            description="Obtiene un usuario según su identificador",
            response_model=UserResponse,
            responses={
                404: {"description": "Usuario no encontrado"}
            })
def get_user(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_by_id(db, user_id)

@router.put("/{user_id}",
            summary="Actualizar usuario",
            description="Actualiza parcialmente un usuario",
            response_model=UserResponse,
            responses={
                404: {"description": "Usuario no encontrado"}
            })
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user)

@router.delete("/{user_id}",
            summary="Eliminar usuario",
            description="Elimina un usuario del sistema",
            status_code=status.HTTP_204_NO_CONTENT,
            responses={
                204: {"description": "Usuario eliminado"},
                404: {"description": "Usuario no encontrado"}
            })
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service.delete_user(db, user_id)
