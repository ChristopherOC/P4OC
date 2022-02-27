from controllers import *
from router import router


#Navigation router
router.add_path("/", main_controller)

#Players router
router.add_path("/players",players_controller)
router.add_path("/player/add",player_form)
router.add_path("/players/list/by-name",list_players_by_name)
router.add_path("/players/list/by-rank",list_players_by_rank)
router.add_path("/players/update-rank",update_player_rank)

#Tournament router
router.add_path("/tournaments", tournaments_controller)
router.add_path("/tournament/add", create_tournament)
router.add_path("/tournaments/list/current", tournament_list)
router.add_path("/tournaments/list/pending", pending_tournament)
router.add_path("/tournaments/reports", tournament_report)

router.navigate('/')


"""
Raport de tournoi :
    * Lister les joueurs du tournoi par ordre alphabétique
    * Lister les joueurs du tournoi par score
    * Lister les tours d'un tournoi (round)*
    * Lister les matchs d'un tournoi (utilisation fstring)

Afficher le nom du round
""" 