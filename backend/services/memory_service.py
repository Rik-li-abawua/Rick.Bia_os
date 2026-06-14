class MemoryService:
    def __init__(self):
        self.items = []

    def save(self, user_id:str, content:str):
        self.items.append({'user_id':user_id,'content':content})
        return True

    def get_all(self):
        return self.items
