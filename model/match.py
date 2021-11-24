from pydantic import validator
from pydantic.main import BaseModel

from player_manager import player_manager as pm


class Match(BaseModel) :

        id_player_1: int
        id_player_2: int
        score_player_1: float
        score_player_2:float


        @validator('id_player_1','id_player_2')
        def check_id_player(cls,value):
            if not isinstance(value,int):
                raise ValueError('must be an int')  
            try:
                pm.search_by_id(value)
            except ValueError:
                raise ValueError(f"This player(id:{value}) don't exist")
            return value

    
            
