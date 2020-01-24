# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move(self, new_location):
        self.current_room = new_location.name.split(' ')[0].lower()

    def take(self, item):
        self.inventory.append(item)

    # def drop(self, item):

    def show_inventory(self):
        print("Inventory: {}".format(self.inventory))