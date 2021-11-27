import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from src.models import NewUser, GetUser
from connection_database.database_tables import User

def create_user(db: Session, user: NewUser):
    
    db_user = User(
        id=random.randint(10000000,99999999),
        names=user.names, 
        last_names=user.last_names, 
        phone_number=user.phone_number,
        cellphone_number=user.cellphone_number, 
        adress=user.adress,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, identificator: int):
    print(db.query(User).filter(User.id == identificator).first())
    return db.query(User).filter(User.id == identificator).first()
