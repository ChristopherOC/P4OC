from model.tournament import Tournament
from views import View, PickWinner
from model.match import Result
from round_manager import round_manager as rm

class PlayTournament:
    def __init__(self,view : View):
        self.view = View
        view.display() 
        
    def play(self):
        self.play = PickWinner(rm.search(filter_key= lambda x :x.score_player_1 == None))
        

    