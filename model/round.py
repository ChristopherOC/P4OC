from datetime import date
from typing import List, Tuple

from pydantic import BaseModel, validator, constr
from manager import Manager


class Round(BaseModel):

    name : constr 
    begin_date : date
    end_date : date  = None
    matchs : List

    # @validator('name')
    # def check_round_name(cls,value):
    #     if not isinstance(value,str):
    #         raise ValueError('Must be a valid name')
    #     return value
    
    # @validator('begin_date')
    # def check_date(cls, value):
    #     if not isinstance(value,datetime):
    #         raise ValueError
    #     return value
    
    # @validator('matchs')
    # def check_matchs(cls,value):
    #     if not isinstance(value,list):
    #         raise ValueError
    #     return value

round_manager = Manager(Round)

# Test = Round(name="testround",begin_date = "2022-06-06 10:00",end_date="2022-06-07 10:00",matchs =[[ 1, 1], [2,0]])
# print(Test)

