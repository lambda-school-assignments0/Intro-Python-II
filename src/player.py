# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, new_location):
        self.current_room = new_location.name.split(' ')[0].lower()

    # def take(self, item):

    # def drop(self, item):

    # def show_inventory(self):