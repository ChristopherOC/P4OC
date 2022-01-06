from datetime import datetime
from typing import List

from pydantic import BaseModel, validator
from pydantic.types import PositiveInt, constr

from player_manager import player_manager as pm
from model.round import Round



class Tournament(BaseModel):
    
    name : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    location : constr( strict= True, regex=  "^[A-Za-z '\-éèàçê]{2,25}$")
    begin_date : datetime = datetime.today()
    end_date : datetime = None
    rounds : List[Round] = []
    players : List[PositiveInt]
    id : PositiveInt

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()
    
    def setup(self):
        pass

    @validator('players')
    def check_players(cls, value):
        if not isinstance(value,list):
            raise ValueError("players don't match")
        for player_id in value:
            if not isinstance(player_id,int):
                raise ValueError('must be an int')  
            try:
                pm.search_by_id(player_id)
            except ValueError:
                raise ValueError(f"This player(id:{player_id}) don't exist")
        return value

    @validator('id')
    def check_id(cls,value):
        if not isinstance(value,int):
            raise ValueError('wrong id')
        return value

    def play(self):

        pass
    
# tourney= Tournament(name="Feraille", location="Tours", date="2021-6-3")
# print(tourney.json())

 
