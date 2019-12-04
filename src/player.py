# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location

    # def move_to(self, location, direction):
    #     new_location = [extension for extension in location if(
    #         extension in direction.name)]
    #     self.location = new_location[0]

        # def defence(self, enemy):
        #     if self > 0 and enemy < 25:
        #         health += enemy

        # def attack(self, enemy):
        #     if enemy > 0 and damage < 25:
        #         damage += enemy
