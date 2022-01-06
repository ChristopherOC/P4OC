# from player_manager import player_manager as pm 
# from views import PickPlayer

from model.match import Match
from views import Menu
import views
from tournament_manager import tournament_manager as tm
from player_manager import player_manager as pm

class UpdatePlayer(Menu):
    def __init__(self):
        
        pm.save_item(player)
        super().__init__(title= "Saisir la nouvelle donnée")

player_id = views.PickPlayer(pm.search(sort_key= lambda x: x.rank)).display()
views.update_data(player_id)
pm.create(player_id)
player = pm.search_by_id(player_id)


# print(PickPlayer(pm.all()).display())

# match_1 = Match(id_player_1 = 1, id_player_2 = 2)
# match_2 = Match(id_player_1 = 2, id_player_2 = 3)
# match_3 = Match(id_player_1 = 5, id_player_2 = 6)
# matchs = [match_1,match_2]
# assert match_3 not in matchs

# tournament_id = views.PickTournament("Pending_Tournament", tm.search(filter_key= lambda x: x.end_date == None)).display()
# tournament = tm.search_by_id(tournament_id)
# views.PendingTournament(tournament_id)