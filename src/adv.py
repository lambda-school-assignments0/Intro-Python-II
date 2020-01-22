import sys
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player("Player 1", "outside")

# Write a loop that:
while True == True:
    # Prints the current room name
    print("Current Location: {}".format(room[my_player.current_room].name))

    # Prints the current description (the textwrap module might be useful here).
    print("{}\n".format(room[my_player.current_room].description))

    # Waits for user input and decides what to do.
    player_input = input("Where do you want to go?\n").lower()

    # If the user enters "q", quit the game.
    if player_input == "q":
        print("Thanks for playing!")
        sys.exit()

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if player_input in ["n", "e", "s", "w"]:
        # If direction is valid, move in that direction
        if hasattr(room[my_player.current_room], "{}_to".format(player_input)):
            my_player.move(eval("room[my_player.current_room].{}_to".format(player_input)))
        # If direction is invalid, print invalid direction error message
        else:
            print("Invalid direction to move!")
    else:
        # Print invalid command error message
        print("Invalid command!")