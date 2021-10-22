import json


class Manager :
  
    def __init__(self, item_type):
        self.items = {}
        self.item_type = item_type



    def from_json(self, path):
        with open(path) as file :
            for item_data in json.loads(file.read()):
                self.create(**item_data)
                
    def create(self,**kwargs):
        item = self.item_type(**kwargs)
        self.items[item.id] = item
        return item

    def search(self,key):
        # print(self.items)
        return dict(filter(key,self.items)).values()

    def search_by_id(self,id):
        return self.items[id]

    # def search_by_name(self,lastname):
    #     return self.items[lastname]
    # def search_by_score(self,rank):
    #     score = []
    #     return self.items[score]

    # def search_by_rank(self):
    #     return sorted(list(self.items.values()), key=lambda x: x.rank)

    def all(self):
        return list(self.items.values())
        