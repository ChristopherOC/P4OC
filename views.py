import json

from model.tournament import Tournament, tournament_manager
import os
from typing import List, Tuple, Any
import enum
from model.player import Player, player_manager



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

class FormTournament(Form): #Formulaire d'un tournoi
    def __init__(self):
        super().__init__(title = "Formulaire du tournoi", fields=[('name','le nom du tournoi', str),
        ('location','le lieu du tournoi', str),
        ('tournament_day','le jour du tournoi', int),
        ('tournament_month','le mois du tournoi', int),
        ("tournament_year","l'année du tournois", int)])





class ListView(View): #lister les joueurs
    def __init__(self, title, items):
        content = "\n".join([str(item) for item in items])
        super().__init__(title ,content, blocking= True)



class PendingTournament(Form):
    def __init__(self):
        super().__init__(title = "Reprise du tournoi")
        
        j = json.dumps()
        with open('tournament.json','w') as f:  
            f.write(j)



# View(title="Tournament", content="Veuillez choisir dans le menu\n", blocking=True).display()
# Menu(title='Menu', choices=['FormPlayer','FormTournament','Exit']).display()
# EnumMenu('EnumMenu', Player.Gender).display()
# FormPlayer().display() 
