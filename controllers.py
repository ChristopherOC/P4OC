import views
from player_manager import player_manager as pm
from router import router
from tournament_manager import tournament_manager as tm


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

def update_player_rank():
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
    print(tm.create(save= True, **form_data))
    router.navigate("/tournaments") 

def tournament_list():
    views.ListView("Tournament", tm.all()).display()
    router.navigate("/tournaments") 

def pending_tournament(): #Boucler tant que c'est pas bon 
    tournament_id = views.PickTournament("Pending Tournament", tm.search(filter_key= lambda x: x.end_date == None)).display()
    tournament = tm.search_by_id(tournament_id)
    tournament.play(pick_winner_view_class = views.PickWinner)
    tm.save_item(tournament.id)
    router.navigate("/tournaments")

def tournament_report():
    tournamernt_id = views.PickTournament("Liste des tournois", tm.all()).display()
    tournament = tm.search(tournamernt_id)
    views.TournamentReport(tournament)


