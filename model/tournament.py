from datetime import datetime
from typing import List

from pydantic import BaseModel, validator
from pydantic.types import PositiveInt, constr
from model.match import Match

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
        if not self.rounds[0].matchs:
            players = [pm.search_by_id(player_id) for player_id in self.players]
            players.sort(key= lambda x: -x.rank)
            group_1 = players[:len(players)//2]
            group_2 = players[len(players)//2:]
            self.rounds[0].matchs = [Match(id_player_1=player_1.id, id_player_2=player_2.id) for player_1, player_2 in zip(group_1, group_2)]


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

    def play(self, pick_winner_view_class, player_manager):#coder les matchs de tournament, round et match
        for round in self.rounds :
            #round.setup pour voir s'il a deja été commencé / pazs de match = aps setup
            round.play(pick_winner_view_class, player_manager)
    
