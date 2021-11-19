from controllers import *
from model.tournament import tournament_manager as tm
from router import router


# player_manager.from_json('ChessPlayers.json')
# tournament_manager.from_json('tournament.json')
# print(player_manager.all())
# controllers.main_controller()
# controllers.players_controller()
# controllers.tournaments_controller()
# controllers.tournaments_form()

#Navigation router
router.add_path("/", main_controller)


#Players router
router.add_path("/players",players_controller)
router.add_path("/player/add",player_form)
router.add_path("/players/list/by-name",list_players_by_name)
router.add_path("/players/list/by-rank",list_players_by_rank)

#Tournament router
router.add_path("/tournaments", tournaments_controller)
router.add_path("/tournament/add",tournament_form)
router.add_path("/tournaments/list/current",tournament_list)
router.add_path("/tournaments/list/pending", pending_tournament)

router.navigate('/')


# db = TinyDB('db.json')
# for fields in views.Form :
#     db.insert({views.Form, views.FormPlayer(fields)})
# print(db)
