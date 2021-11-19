import datetime
from typing import List
from manager import Manager
from pydantic import BaseModel, validator

from player_manager import player_manager as pm
from model.round import Round


class Tournament(BaseModel):
    
    name : str
    location : str
    begin_date : str = None
    end_date : str = None
    rounds : List[Round]
    players : list
    id : int = None
    
     
    @validator('name')
    def check_tournament_name(cls, value):
        if not isinstance(value, str):
            raise ValueError('Must be a valid name')
        return value
    
    @validator('location')
    def check_location(cls, value):
        if not isinstance(value, str):
            raise ValueError('Must be a valid location')
        return value
    
    @validator('begin_date')
    def check_begin_date(cls,value):
        if not value :
            value = datetime.datetime()
        try:
            value = datetime.fromisoformat(value)
        except ValueError:
            raise ValueError('wrong format')
        
        return value

    @validator('begin_date','end_date')    
    def check_if_date_ok(cls,value):
        if not (isinstance(value,str) or isinstance(value, datetime)):
            raise ValueError('must be a string or datetime')
        return value

    @validator('end_date')
    def check_end_date(cls,value,values):
        if not (isinstance(value,str) or isinstance(value,datetime)):
            raise ValueError('must be a string')
        # if value < values:
        #     raise ValueError("dates don't match")
        return value



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

    
# tourney= Tournament(name="Feraille", location="Tours", date="2021-6-3")
# print(tourney.json())

 
