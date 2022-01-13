from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, constr
from model.match import Match


class Round(BaseModel):

    name : constr(strict= True, min_length= 1, max_length=15) 
    begin_date : Optional[datetime] = datetime.today() 
    end_date : datetime  = None
    matchs : List[Match] = []

  

