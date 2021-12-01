"""Création d'un programme ayant pour but d'organiser un tournoi d'échec
"""
from datetime import datetime, date, timedelta
from enum import Enum
from os import error

from pydantic import BaseModel, validator, PositiveInt
from pydantic.types import conint, constr


class Gender(Enum):
    Male = "M"
    Female = "F"


class Player(BaseModel) :
#Création d'une classe Player


    lastname : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    firstname : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    birthdate : date
    rank : conint(strict= True, gt = 0, lt = 3000)
    sexe : Gender 
    id : PositiveInt 
                
    # @validator("birthdate")
    # def check_if_birthdate_is_valid(cls,value):
    #     if not isinstance(value, date):
    #         raise ValueError('Format error')
    #     age =  date.today() - value
    #     if age < date.timedelta(4380):
    #         raise error('Too young')
    #     return value

    
    def __str__(self) -> str:
        return f'{self.firstname},{self.lastname},{self.rank}'



