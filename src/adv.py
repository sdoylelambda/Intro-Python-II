from room import Room
from player import Player
from item import Item

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

# Items

items = {
    'dagger': Item("dagger", """dagger"""),
    'sword': Item("sword", """sword dagger"""),
    'potion': Item("Heal Potion", """Heal Potion recovers 5hp"""),
    'lightning': Item("Lightning Rune", """Gives magic ability lightning"""),
    'fire': Item("Fire Rune", """Gives magic ability fire"""),
}

for i in items:
    print(i)
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items
dagger = Item("dagger", items['dagger'])
print(dagger)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input("Enter Name:"), room['outside'])
# print(room['outside'].n_to)
# print(player)

print("Prepare yourself for the most thrilling game ever", player.name, "!!!")
print(player.currentRoom)
print("\nEnter a command!(n, s ,e ,w ,q)")

directions = ["n", "s", "w", "e", "q"]

# Write a loop that:
while True:
    # Read command
    cmd = input("~~> ").lower()
    # Check if it's n/s/e/w/q
    if cmd in directions:
        # Make player travel in that direction
        player.travel(cmd)
        print(dagger)
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        exit()
    else:
        print("I did not recognize that command")

# * Prints the current description (the textwrap module might be useful here).
    # print(Room.description)
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.


#
#     if cmd in directions:
#         if hasattr(player.currentRoom, F"{cmd}_to") is None:
#             player.travel(cmd)
#             # player.currentRoom = getattr(player.currentRoom, F"{cmd}_to")
#             print("can't go that way")
#         else:
#             print("can't go that way")
#             pass
#     else:
#         print("or that way")
#
#     if cmd == 'n' and hasattr(player.currentRoom, "n_to"):
#         # and room.n_to === :
#         # print('going north')
#         # player.currentRoom == room['foyer']
#         # print('room:::', room['foyer'])
#         player.currentRoom = getattr(player.currentRoom, F"{cmd}_to")
#         print(player.currentRoom)
#         continue
#         # print(room['outside'])
#     elif cmd == 's':
#         player.currentRoom = getattr(player.currentRoom, F"{cmd}_to")
#         print(player.currentRoom)
#     elif cmd == 'e':
#         print('go east')
#         player.currentRoom = getattr(player.currentRoom, F"{cmd}_to")
#         print(player.currentRoom)
#     elif cmd == 'w':
#         print('go west')
#         player.currentRoom = getattr(player.currentRoom, F"{cmd}_to")
#         print(player.currentRoom)
#     elif cmd == 'q':
#         print("Goodbye!")
#         break
#     else:
#         print("Enter a valid command!(n, s ,e ,w ,q)")
# #



# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# NEED INPUT -- RPS APP -- CHECK VIDEO

# STRING METHOD

# HINT -- INFO TO ADD TO A LIST
