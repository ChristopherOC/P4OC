
from manager import Manager
from router import router
import views
from player_manager import player_manager as pm
from tournament_manager import tournament_manager as tm


def main_controller():
    print('in main controller')
    router.navigate(views.MainMenu().display())


#For the players

def players_controller():
    print('in players controller')
    router.navigate(views.PlayerMenu().display())


def player_form():
    print("In the player form")
    views.FormPlayer().display()
    router.navigate("/players")


def list_players_by_name():
    print("In the player list")
    views.ListView("Players",pm.search(sort_key = lambda x: x.lastname)).display() 
    router.navigate("/players")


def list_players_by_rank():
    print("In the player list")
    views.ListView("Players",pm.search(sort_key = lambda x: -x.rank)).display() 
    router.navigate("/players")

# def update_player_rank():
#     print("Updating player rank's")
#     updating = pm.search(filter_key= lambda x: x.rank) à compléter
    # Manager.save_item()
    # router.navigate("/players")

# For the tournament
def tournaments_controller():
    print('in tournament controller')
    router.navigate(views.TournamentMenu().display())


def tournament_form():
    print("In the Form Tournament")
    views.FormTournament().display()
    players = [] ### Insert des joueurs à la création du tournoi 
    player = views.FormPlayer().display()
    while len(players) < 8 :
        input(views.FormPlayer().display())
        router.navigate("/tournaments")
        players.append(player)
        if len(players) == 8 :
            router.navigate(views.MainMenu().display())
            print("Assez de joueurs enregistrés")
    router.navigate("/tournaments") 

def tournament_list():
    print("In the tournament list")
    views.ListView("Tournament", tm.all()).display()
    router.navigate("/tournaments") 

def pending_tournament(): #Boucler tant que c'est pas bon 
    print("In the pending tournaments")
    print(tm.all())
    tournaments = tm.search(filter_key = lambda x: x.end_date == None)

    print(tournaments)

  
    # while True:
    #     form_data = views.Form("Tournoi à reprendre", fields=[("id","id",int)]).display()
    #     tournament = tournament_manager.search(form_data["id"])    
    #     router.navigate("/tournaments")


    #Moyen de savoir si le tournoi est terminé ou peut etre continué
    #Modifier le modele du tournoi "end_date" ,null 
    #Gérer TinyDB