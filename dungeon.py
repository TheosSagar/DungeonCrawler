import random
from enemy import Skeleton, Goblin, Dragon


class Dungeon:
    """Creates encounters and tracks the player's progress through rooms."""

    def __init__(self):
        self.room_number = 0
        self.total_rooms = 5

    def next_encounter(self):
        self.room_number += 1

        if self.room_number == self.total_rooms:
            return Dragon()

        enemy_class = random.choice([Skeleton, Goblin])
        return enemy_class()

    def is_final_room(self):
        return self.room_number == self.total_rooms
