from Map import Map

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location_id = location
        self.inventory = []
        self.map = Map()
        self.map.create_rooms()
    
    def get_current_room(self):
        return self.map.get_room(self.location_id)