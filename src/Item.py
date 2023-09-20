class Item:
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable
    
    def get_name(self):
        return self.name