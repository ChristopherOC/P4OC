import json
from typing import List

from tinydb import TinyDB, table
from tinydb.table import Document

class Manager :
  
    def __init__(self, item_type):
        self.items = {}
        self.item_type = item_type
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(self.item_type.__name__.lower() + "s")
        for item_data in  self.table :
            self.create(**item_data)

    # def from_json(self, path):
    #     with open(path) as file :
    #         for item_data in json.loads(file.read()):
    #             self.create(**item_data)
                
    def create(self,save =  False,**kwargs):
        if "id" not in kwargs:
            kwargs["id"]= self.table.all()[-1].doc_id +1
        
        item = self.item_type(**kwargs)
        self.items[item.id] = item
        if save :
            self.save_item(item.id)
        return item
        

    def search(self,filter_key = lambda x: x, sort_key = lambda x: x):
        # print(self.items)
        return list(sorted(filter(filter_key,self.items.values()),key = sort_key))


    def search_by_id(self,id):
        return self.items[id]

    def all(self):
        return list(self.items.values())
  
    def save_item(self, id):
        item = self.find_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))   

   # def search_by_name(self,lastname):
    #     return self.items[lastname]
    # def search_by_score(self,rank):
    #     score = []
    #     return self.items[score]

    # def search_by_rank(self):
    #     return sorted(list(self.items.values()), key=lambda x: x.rank)