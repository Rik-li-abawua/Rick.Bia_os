import os

class MotherDuckService:
    def __init__(self):
        self.token = os.getenv('MOTHERDUCK_TOKEN')
