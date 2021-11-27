from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy_utils.types.choice import ChoiceType


from .database_connection import Base

class User(Base):
    
    __tablename__ = "wordbox_users"
    
    id = Column(Integer, primary_key=True)
    names = Column(String)
    last_names=Column(String)
    phone_number = Column(String, default=True)
    cellphone_number = Column(String, default=True)
    adress = Column(String, default=True)