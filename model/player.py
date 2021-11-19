"""Création d'un programme ayant pour but d'organiser un tournoi d'échec
"""
import datetime
import re
from enum import Enum
from os import error

from manager import Manager
from pydantic import BaseModel, validator


class Player(BaseModel) :
#Création d'une classe Player

    class Gender(Enum):
        Male = "M"
        Female = "F"

    lastname : str 
    firstname : str 
    birthdate : datetime.date
    rank : int 
    sexe : Gender 
    id : int = None


    @validator("lastname","firstname")
    def check_if_name_is_str(cls,value):
        if isinstance(value, str) :
            pattern = "^[A-Za-z '\-éèàçê]{2,25}$"
            if not re.match(pattern,value):
                raise ValueError('Must be a valid name')
        else :
            raise ValueError('Must be a string')

        return value
                
    @validator("birthdate")
    def check_if_birthdate_is_valid(cls,value):
        if not isinstance(value, datetime.date) :
            raise ValueError('Format error')
        age =  datetime.date.today() - value
        if age < datetime.timedelta(4380):
            raise error('Too young')
        return value

    @validator("rank")
    def check_if_rank_is_int(cls, value):
        if not isinstance(value,int):
            print(value)
        if value < 0 or value > 3000  :
            raise ValueError('The rank must be between 0 and 3000')
        return value
        

    @validator("sexe")
    def check_if_sexe_is_valid(cls, value):
        if isinstance(value, str):
            try : 
                value = Player.Gender(value)
            except ValueError:
                print('must be Male or Female')

        if isinstance(value,Player.Gender): 
            return value.name



    @validator("id")
    def check_if_id_is_valid(cls, value):
        if not isinstance(value, int):
            raise ValueError('id already used or wrong format')
        return value
    
    def __str__(self) -> str:
        return f'{self.firstname},{self.lastname},{self.rank}'



