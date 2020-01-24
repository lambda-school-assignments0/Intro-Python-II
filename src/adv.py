import sys
import os
from item import Item
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    # TODO: Grand Overlook is broken because first word is not Overlook...
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'chasm':     Room("Chasm", """Against every fiber of your being, a mysterious
force compels you to move further north. Unable to resist the decisions of the gods,
you tumble down into the bottomless chasm to your death. [GAME OVER]"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'secret':   Room("Secret Vault", """Stumbling through the secret corridor,
you find yourself face to face with a slumbering dragon. It stirs as it hears you enter
its domain. You only have a split-second to act.""")
}

# Declare all the items

item = {
    'gold': Item("Gold", """A single gold coin with an elaborate design on both sides"""),
    'map': Item("Map", """A treasure map with a single red 'x' marked on a continent across the ocean"""),
    'sword': Item("Sword", """A razor sharp sword, smeared with dragon's blood"""),
    'torch': Item("Torch", """A torch that doesn't seem to burn to the touch and gives off a faint glow"""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['chasm']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].items = [item['sword']]
room['overlook'].items = [item['torch']]
room['secret'].items = [item['gold'], item['map']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player("Player 1", "outside")

# Clear console for readability
os.system('cls')

# Write a loop that:
while True == True:
    # Prints the current room name
    print("Current Location: {}".format(room[my_player.current_room].name))

    # Prints the current description (the textwrap module might be useful here).
    print("Description: {}".format(room[my_player.current_room].description))

    # Prints the items in the current room
    print("Items: {}\n".format([item.name for item in room[my_player.current_room].items]))

    # Waits for user input and decides what to do.
    player_input = input("What do you do now?\n(type 'help' for more info)\n").lower()

    # Clear console for readability
    os.system('cls')

    # If the user enters "q", quit the game.
    if player_input == "q":
        print("Thanks for playing!")
        sys.exit()

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if (player_input.split(' ')[0] == "m" or player_input.split(' ')[0] == "move") and player_input.split(' ')[1] in ["n", "e", "s", "w"]:
        # If direction is valid, move in that direction
        if hasattr(room[my_player.current_room], "{}_to".format(player_input.split(' ')[1])):
            my_player.move(eval("room[my_player.current_room].{}_to".format(player_input.split(' ')[1])))
        # If direction is invalid, print invalid direction error message
        else:
            print("Invalid direction to move!")
    elif player_input.split(' ')[0] == "t" or player_input.split(' ')[0] == "take":
        # TODO: If item is available, take item
        if item[player_input.split(' ')[1]] in room[my_player.current_room].items:
            my_player.take(player_input.split(' ')[1])
        # TODO: If item is unavailable, print unavailable item error message
        else:
            print("There is no {} in this room!".format(player_input.split(' ')[1]))

    # elif player_input.split(' ')[0] == "d" or player_input.split(' ')[0] == "drop":
        # TODO: If item is available, drop item

        # TODO: If item is unavailable, print unavailable item error message

    elif player_input == "i" or player_input == "inv" or player_input == "inventory":
        # Print out player's inventory
        my_player.show_inventory()

    # elif player_input == "h" or player_input == "help" or player_input == "commands":
        # TODO: Print out help prompt

    else:
        # Print invalid command error message
        print("Invalid command!")

    