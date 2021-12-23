
from datetime import datetime
from manager import Manager
from matchmaking import Matchmaking
# from play_tournament import PlayTournament
from router import router
import views
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm
# from play_tournament import PlayTournament as pt
from round_manager import round_manager as rm


def main_controller():
    print('in main controller')
    router.navigate(views.MainMenu().display())


#For the players

def players_controller():
    print('in players controller')
    router.navigate(views.PlayerMenu().display())


def player_form():
    print("In the player form")
    form_data = views.FormPlayer().display()
    pm.create(save= True, **form_data)
    router.navigate("/players")


def list_players_by_name():
    print("In the player list")
    views.ListView("Players",pm.search(sort_key = lambda x: x.lastname)).display() 
    router.navigate("/players")


def list_players_by_rank():
    print("In the player list")
    views.ListView("Players",pm.search(sort_key = lambda x: -x.rank)).display() 
    router.navigate("/players")

def update_player_rank():#terminer
    print("Updating player rank's")
    #pickplayer, reécupérer, modifié, et sauvegarder
    updating = pm.search(filter_key= lambda x: x.rank)
    router.navigate("/players")

# For the tournament
def tournaments_controller():
    print('in tournament controller')
    router.navigate(views.TournamentMenu().display())



def tournament_form():#create
    print("In the Form Tournament")
    form_data = views.FormTournament().display()
    players = [] ### Insert des joueurs à la création du tournoi 
    player = views.FormPlayer().display()
    while len(players) < 8 :
        input(views.FormPlayer().display())
        router.navigate("/tournaments")
        players.append(player)
        if len(players) == 8 :
            router.navigate(views.MainMenu().display())
            print("Assez de joueurs enregistrés")
    form_data["players"] = players
    tm.create(save= True, **form_data)
    router.navigate("/tournaments") 

def tournament_list():
    print("In the tournament list")
    views.ListView("Tournament", tm.all()).display()
    router.navigate("/tournaments") 

def pending_tournament(): #Boucler tant que c'est pas bon 
    print("In the pending tournaments")
    # search_not_ended = tm.search(filter_key= lambda x: x.end_date == None)
    # input(search_not_ended)
    tournament_id = views.PickTournament("Pending_Tournament", tm.search(filter_key= lambda x: x.end_date == None)).display()
    tournament = tm.search_by_id(tournament_id)
    print(tournament)

    # Matchmaking.gen_turn_one()
    # Matchmaking.gen_next_turn()
    
    #pick un tounoi

    router.navigate("/tournaments")
  
    # while True:
    #     form_data = views.Form("Tournoi à reprendre", fields=[("id","id",int)]).display()
    #     tournament = tournament_manager.search(form_data["id"])    
    #     router.navigate("/tournaments")

