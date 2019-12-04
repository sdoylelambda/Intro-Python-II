# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init(room, health, damage):
        self.room = room
        self.health = health
        self.damage = damage

        def location(self, room):
            if room == 'outside':
                print(room.Room)
            elif room == 'foyer':
                print(room.Room)
            elif room == 'overlook':
                print(room.Room)
            elif room == 'narrow':
                print(room.Room)
            elif room == 'treasure':
                print(room.Room)
            else:
                print('You are lost')

        def defence(self, enemy):
            if self > 0 and enemy < 25:
                health += enemy

        def attack(self, enemy):
            if enemy > 0 and damage < 25:
                damage += enemy
