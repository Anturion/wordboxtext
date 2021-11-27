from fastapi import APIRouter
from fastapi import Request
from sqlalchemy.orm import Session
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY
)
from fastapi import Depends, FastAPI, HTTPException, status
from src.models.user import NewUser, GetUser
from src.services.user import create_user, get_user_by_id
from connection_database.database_connection import SessionLocal, engine_azure

registry_routes = APIRouter(prefix='/register', tags=['Register'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@registry_routes.post("/user", status_code=HTTP_201_CREATED)
def register_user(user: NewUser, db: Session = Depends(get_db)):
    """
    Validates format data and create the user if the data is correct.
    :param user: contains all the information about a user
    """
    user_created = create_user(db=db, user=user)
    if user_created:
        return {
                'message': 'Usario creado correctamente',
                'id': user_created.id
                }
    raise HTTPException(status_code=404, detail="Algo salió mal")

@registry_routes.get("/users/", response_model=GetUser)
def read_users(identificator: int = 0, db: Session = Depends(get_db)):
    """Take an integer as a parameter and search the user that its primary
    kay match with de parameter

    Args:
        identificator: an id to search user in database

    Returns:
        Model pydantic GetUser
    """
    user = get_user_by_id(db, identificator=identificator)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
