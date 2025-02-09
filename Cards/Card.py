# Card class that will be used for each card metadata
class Card():
    def __init__(self, name):
        self.name = name
    
    def get_name(self) -> str:
        return self.name