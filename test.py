# from player_manager import player_manager as pm 
# from views import PickPlayer

from model.match import Match

# print(PickPlayer(pm.all()).display())

match_1 = Match(id_player_1 = 1, id_player_2 = 2)
match_2 = Match(id_player_1 = 2, id_player_2 = 3)
match_3 = Match(id_player_1 = 5, id_player_2 = 6)
matchs = [match_1,match_2]
assert match_3 not in matchs