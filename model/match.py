from pydantic import validator
from pydantic.main import BaseModel
from enum import Enum

from player_manager import player_manager as pm

class Result(Enum):
    Win = 1.0
    Loose = 0.0
    Draw = 0.5

    

class Match(BaseModel) :

        id_player_1: int
        id_player_2: int
        score_player_1: Result = None
        
        @property 
        def score_player_2(self):
            return Result(1.0 - self.score_player_1.value) if self.score_player_1 else None


        @validator('id_player_1','id_player_2')
        def check_id_player(cls,value):
            if not isinstance(value,int):
                raise ValueError('must be an int')  
            try:
                pm.search_by_id(value)
            except ValueError:
                raise ValueError(f"This player(id:{value}) don't exist")
            return value


    
            
