# from player_manager import player_manager as pm 
# from views import PickPlayer


from result import Result
import views
from model.match import Match
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm
from views import Menu

match = Match(id_player_1=1, id_player_2=3, score_player_1 = 1.0)



if match.is_played:
    print(match)
    if match.has_player(player_id = 1):
        
        print(type(match.get_player_score(player_id = 1)))
    