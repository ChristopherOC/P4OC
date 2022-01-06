# from play_tournament import PlayTournament
from router import router
import views
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm
# from play_tournament import PlayTournament as pt
from round_manager import round_manager as rm
from match_manager import match_manager as mm


def main_controller():
    router.navigate(views.MainMenu().display())


#For the players

def players_controller():
    router.navigate(views.PlayerMenu().display())


def player_form():
    form_data = views.FormPlayer().display()
    pm.create(save= True, **form_data)
    router.navigate("/players")


def list_players_by_name():
    views.ListView("Players",pm.search(sort_key = lambda x: x.lastname)).display() 
    router.navigate("/players")


def list_players_by_rank():
    views.ListView("Players",pm.search(sort_key = lambda x: -x.rank)).display() 
    router.navigate("/players")

def update_player_rank():#terminer
    #pickplayer, reécupérer, modifié, et sauvegarder
    player_id = views.PickPlayer(pm.search(sort_key= lambda x: x.rank)).display()
    player = pm.search_by_id(player_id)
    form_data = views.UpdatePlayer().display()
    player.rank = form_data["rank"]
    pm.save_item(player_id)
    
    router.navigate("/players")

# For the tournament
def tournaments_controller():
    router.navigate(views.TournamentMenu().display())



def create_tournament():#create
    form_data = views.FormTournament().display()
    players = [] ### Insert des joueurs à la création du tournoi 
    player = views.PickPlayer().display()
    while len(players) < form_data["number_of_players"] :
        input(views.FormPlayer().display())
        router.navigate("/tournaments")
        players.append(player)
        if len(players) == form_data["number_of_players"] :
            router.navigate(views.MainMenu().display())
            print("Assez de joueurs enregistrés")
    form_data["players"] = players
    form_data["rounds"] = [{"name" : f'Round{round_nb}'} for round_nb in range(1,form_data["number_of_rounds"]+1)]
    print(tm.create(save= True, **form_data))
    router.navigate("/tournaments") 

def tournament_list():
    views.ListView("Tournament", tm.all()).display()
    router.navigate("/tournaments") 

def pending_tournament(): #Boucler tant que c'est pas bon 
    tournament_id = views.PickTournament("Pending Tournament", tm.search(filter_key= lambda x: x.end_date == None)).display()
    tournament = tm.search_by_id(tournament_id)
    rounds_matchs = tm.search(filter_key= lambda x: x.score_player_1 == None)
    tournament_matchs = views.PickWinner().display()
    print(tournament_matchs)
    views.PendingTournament(tournament).display()

    print(tournament)

    # Matchmaking.gen_turn_one()
    # Matchmaking.gen_next_turn()
    
    #pick un tounoi

    router.navigate("/tournaments")
  
    # while True:
    #     form_data = views.Form("Tournoi à reprendre", fields=[("id","id",int)]).display()
    #     tournament = tournament_manager.search(form_data["id"])    
    #     router.navigate("/tournaments")

