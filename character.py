class Character:

    def __init__ (self, name, health, attack_damage, defence):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.defence = defence

    def status(self):
        return(
            f"Character: {self.name}\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack_damage}\n"
            f"Defence: {self.defence}\n"
        )

player = Character("Sagar", 80, 10, 50)
skeleton = Character("Skeleton", 30, 20, 10)
dragon = Character("Dragon", 100, 40, 20)

print(player.status())
print(skeleton.status())
print(dragon.status())