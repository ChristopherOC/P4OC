"""Création d'un programme ayant pour but d'organiser un tournoi d'échec
"""
from datetime import datetime, date, timedelta
from enum import Enum
from os import error

from pydantic import BaseModel, validator, PositiveInt
from pydantic.types import conint, constr

from gender import Gender


class Player(BaseModel) :
    lastname : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    firstname : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    birthdate : date
    rank : conint(strict= True, gt = 0, lt = 3000)
    sexe : Gender 
    id : PositiveInt 
    
    def __str__(self) -> str:
        return f'{self.firstname},{self.lastname},{self.rank}'



