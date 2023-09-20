from Room import Room
from Item import Item
import RoomIds 


class Map:

    def __init__(self) -> None:
        self.rooms = {}

    def create_rooms(self):
        self.create_closet()
        self.create_control_room()
        self.create_airlock()
        self.create_outterspace()
        self.create_exits()

    def create_closet(self):
        shelf = Item("shelf", "The shelf is empty.", False)
        uniform = Item("uniform", "The uniform is blue and drab.", True)
        self.create_room(RoomIds.CLOSET_ID, "The Closet", "You are in a small nondescript closet.", [shelf, uniform])

    def create_control_room(self):
        # Control Room Items
        guard = Item("guard", "The guard looks mean and menacing.", False)
        electronic_lock = Item("lock", "The lock is in front of a large door to the east.", "False")
        credential = Item("credential", "The credential is silver with a barcode on it.", True)
        self.create_room(RoomIds.CONTROL_ROOM_ID, "The Control Room", "You are in a small room that looks like it controls something. There is an airlock to the east.", [guard, electronic_lock, credential])

    def create_airlock(self):
        # Airlock Items
        spacesuit = Item("spacesuit", "The spacesuit looks old, but safe.", True)
        button = Item("button", "The big red button has a warning symbol on it.", False)
        self.create_room(RoomIds.AIRLOCK_ID, "The Airlock", "You are in a small room that is clearly an airlock. There is a window to space in the east. There is an airlock door to the west.", [spacesuit, button])
        
    def create_outterspace(self):
        #outspace items
        cord = Item("cord", "The cord will keep us attached to the spaceship.", True)
        self.create_room(RoomIds.OUTTERSPACE_ID, "Outerspace", "You see the vastness of space and a floating cord...", [cord])

    def create_exits(self):
        control_room = self.rooms[RoomIds.CONTROL_ROOM_ID]
        closet = self.rooms[RoomIds.CLOSET_ID]

        control_room.add_exit(RoomIds.CLOSET_ID, closet)
        closet.add_exit(RoomIds.CONTROL_ROOM_ID, control_room)

    def create_room(self, room_id, name, description, items):
        room = Room(name, description, items)
        self.rooms[room_id] = room

    def get_room(self, room_id):
        return self.rooms.get(room_id)
