from datetime import date, datetime
from typing import Dict, List, Tuple, Any
import enum

from manager import Manager
from model.tournament import Tournament
from tournament_manager import tournament_manager as tm
from player_manager import player_manager as pm


from model.player import Player




class View:

    def __init__(self, title: str, content: str = '',
     blocking: bool = False): #affichage avec séparation du titre en majuscule et du contenu
        self.title = title.upper()
        self.content = content
        self.blocking = blocking

    def display(self):#Affichage de la séparation + efface la console lors de l'exécution
        if self.title: 
            # os.system('cls')
            print(self.title)
            print('*' * len(self.title))
        print(self.content)
        if self.blocking :
            input()

class Menu(View): #Sélection des menu
    def __init__(self, title: str, choices: List[Tuple[str, Any]]):
        content = "\n".join([f'{i} : {desc}' for i, (desc, _) in enumerate(choices, start=1)])
        super().__init__(title, content)
        self.choices  = [value for (_, value) in choices]



    def display(self):
        super().display()
        while True : 
            choice = input('Veuillez saisir votre choix : ')
            if choice.isnumeric():
                if 0 <= int(choice) - 1 < len(self.choices):
                    return self.choices[int(choice) - 1]
                    
            
class MainMenu(Menu):
    def __init__(self):
        super().__init__("ChessMaker", 
            [("Gérer les joueurs", "/players"),
            ("Gérer les tournois", "/tournaments"),
            ("Quitter",  "/quit")]) 


class Form(View): #Formulaire générique qui enregistre les éntrées pour chaque champs
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        super().__init__(title)
        self.fields = fields



    def display(self):
        super().display()
        data = {}
        for name, desc, _type in self.fields:  
            while True:
                if isinstance(_type(), EnumMenu):
                    data[name]= _type().display()
                    break
                try :
                    data[name] = _type(input("Veuillez saisir " + desc + "\n"))
                    if isinstance(data[name],str):
                        if not data[name] : 
                            raise ValueError()
                    break
                except ValueError:
                    print('Valeur spécifiée incorrecte')
        return self.process_data(data)

    def process_data(self, data : Dict):
        return data


class PlayerMenu(Menu): #Menu du joueur
    def __init__(self):
        super().__init__("Gestion des joueurs", 
            [("Lister les joueurs par nom", "/players/list/by-name"),
            ("Lister les joueurs par classement", "/players/list/by-rank"),
            ("Déclarer un joueur", "/player/add"),
            ("Mettre à jour le classement d'un joueur","/players/update-rank"),
            ("Retour",  "/")]) 

class FormPlayer(Form): #Formulaire d'un joueur

    def __init__(self):
        super().__init__("Nouveau Joueur", fields=[("name","le prénom du joueur", str),
        ("lastname","le nom de famille du joueur", str),
        ("rank",  "le rang du joueur", int),
        ("birthdate_year","l'année de naissance du joueur", str),
        ("birthdate_month","le mois de naissance du joueur", str),
        ("birthdate_day","le jour de naissance du joueur", str),
        ("sexe","le sexe du joueur",GenderMenu)])

    def process_data(self, data : Dict):
        data["birthdate"] = date(year = data["birthdate_year"], month =data["birthdate_month"] , day =data["birthdate_day"] )

        return data


class EnumMenu(Menu):#Complète le formulaire d'un joueur pour le sexe
    def __init__(self, title: str, enum: enum.Enum):
        choices = [(e.name, e) for e in enum]

        super().__init__(title, choices)

class GenderMenu(EnumMenu):
    def __init__(self):
        super().__init__("",Player.Gender)



class TournamentMenu(Menu):#Menu du tournoi
    def __init__(self):
        super().__init__("Gestion des tournois",
        [("Liste des tournois en cours","/tournaments/list/current"),
        ("Créer un nouveau tournoi", "/tournament/add"),
        ("Reprendre un tournoi", "/tournaments/list/pending"),
        ("Retour","/")])

    def process_data(self, data : Dict):
        data["begin_date"] = datetime(year = data["tournament_year"], month =data["tournament_month"] , day =data["tournament_day"])
        return data

class FormTournament(Form): #Formulaire d'un tournoi
    def __init__(self):
        super().__init__(title = "Formulaire du tournoi", fields=[
            ('name','le nom du tournoi', str),
            ('location','le lieu du tournoi', str),
            ("number_of_players", "Nombre de joueur",int),
            ("number_of_rounds", "Nombre de rounds", int)])
        
    def process_data(self, data: Dict):
        data["players"] = [PickPlayer(pm.all()).display() for _ in range(data["number_of_players"])]
        data["rounds"] = [{"name" : f'Round{round_nb}',"begin_date" : datetime.today() if round_nb == 1 else None} for round_nb in range(1,data["number_of_rounds"]+1)]
        return data


class PendingTournament(Form): #Process data pour la date renseignée 
    def __init__(self):
        super().__init__(title = "Reprise du tournoi", fields = [("end_date_year", "année de fin du tournoi", str),
        ("end_date_month", "mois de fin du tournoi",str),
        ("end_date_day", "jour de fin de tournoi",str)])


class ListView(View): #lister les joueurs
    def __init__(self, title, items):
        content = "\n".join([str(item) for item in items])
        super().__init__(title ,content, blocking= True)


class PickTournament(Menu):
        def __init__(self, title: str, tournaments: List[Tournament]):
            choices = [(tournament.name, tournament.id) for tournament in tournaments]
            super().__init__(title, choices)
            
            
class PickWinner(Menu):#a terminer
    def __init__(self, player_1 : Player, player_2: Player ):
        choices = [(f"{player_1.firstname} {player_1.lastname} a gagné ", 1.0),
        (f"{player_2.firstname} {player_2.lastname} a gagné ",0.0 ),
        f"égalité", 0.5]
        super().__init__(title = "Choix du gagnant", choices = choices)


class PickPlayer(Menu):
    def __init__(self, players : List[Player]):
        choices = [(str(player), player.id) for player in players]
        super().__init__(title= "Choisissez un joueur", choices = choices)


class UpdatePlayer(Form):
    def __init__(self):
        super().__init__(title= "Saisir la nouvelle donnée", fields= [("rank", "nouveau classement", int)])