class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = items
        self.option = {}

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def add_item(item):
        self.item.append(items)

    def add_exit(self, id, exit):
        self.exits[id] = exit

    def get_exits(self):
        return self.exits

    def get_items(self):
        return self.items

    
