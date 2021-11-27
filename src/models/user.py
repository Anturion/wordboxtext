import re
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator, EmailStr

ALPHANUMERIC = r'^[a-zA-ZñÑ\s]+$'
PHONE_FORMAT = r'^\+[\d]{1,13}$'
FORMAT_DATE = r'^\d{4}-\d{2}-\d{2}$'

class NewUser(BaseModel):

    names : str = Field(...)
    last_names : str = Field(...)
    phone_number : str = Field(...)
    cellphone_number : str = Field(...)
    adress : str = Field(...)
    
    class Config:
        fields = {
            'names': {'max_length': 64, 'regex': ALPHANUMERIC},
            'last_names': {'max_length': 64, 'regex': ALPHANUMERIC},
            'phone_number': {'max_length': 13, 'regex': PHONE_FORMAT},
            'cellphone_number': {'max_length': 64, 'regex': PHONE_FORMAT},
        }
        
class GetUser(NewUser):
    
    id : int
    
    class Config:
        
        orm_mode = True