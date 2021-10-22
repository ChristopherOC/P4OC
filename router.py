from os import path
from typing import Callable


class Router : 
    def __init__(self):
        self.routes = {}
    
    def add_path(self, path:str, controller : Callable):
        self.routes[path] = controller


    def navigate(self, path):
        print(path)
        if path in self.routes.keys():
            print(path)
            self.routes[path]()

router = Router()