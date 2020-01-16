# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def travel(self, direction):
        next_room = self.currentRoom.get_room_in_direction(direction)
        if next_room is not None:
            self.currentRoom = next_room
            print(self.currentRoom)
        else:
            print("You cannot move in that direction.")


    # ADD METHODS
    # def get_name(self):
    #     return self.name
    #
    # def get_location(self):
    #     return self.currentRoom
    #
    # def set_location(self, newLocation):
    #      self.currentRoom = newLocation
    #
    # def __str__(self):
    #     return (f'{self.name}, {self.currentRoom}')