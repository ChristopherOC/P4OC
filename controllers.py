from pydantic import fields
from router import router
import views
from model.player import Player, player_manager
from model.tournament import tournament_manager

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
    print(player_manager.search(lambda x: x.lastname))
    views.ListView("Players",player_manager.search(lambda x: x.lastname)).display() #fonctiuonne plus
    router.navigate("/players")

def list_players_by_rank():
    print("In the player list")
    views.ListView("Players",player_manager.search(item for item in player_manager.items if item["rank"])).display() # fonctionne plus
    router.navigate("/players")

# For the tournament
def tournaments_controller():
    print('in tournament controller')
    router.navigate(views.TournamentMenu().display())

def tournament_form():
    print("In the Form Tournament")
    views.FormTournament().display()
    players = [] ### Insert des joueurs à la création du tournoi /// ajouter la possibilité d'arrêter d'ajouter des joueurs
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
    views.ListView("Tournament", tournament_manager.all()).display()
    router.navigate("/tournaments")
    
def pending_tournament(): #Boucler tant que c'est pas bon 
    print("In the pending tournaments")
    form_data = views.Form("Tournoi à reprendre", fields=[("id","id",int)]).display()
    tournament = tournament_manager.search(form_data["id"])
    #Moyen de savoir si le tournoi est terminé ou peut etre continué
    
    #Gérer TinyDB
    

    # views.PendingTournament()
    router.navigate("/tournaments")

