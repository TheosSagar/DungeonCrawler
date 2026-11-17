class Item:
    def __init__(self, name):
        self.name = name


class Potion(Item):
    def __init__(self, healing=35):
        super().__init__("Health Potion")
        self.healing = healing

    def use(self, player):
        return player.use_potion()


class Weapon(Item):
    def __init__(self, name, bonus_damage, price):
        super().__init__(name)
        self.bonus_damage = bonus_damage
        self.price = price
