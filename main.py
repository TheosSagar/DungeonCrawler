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
            f"Defence: {self.defence}"
        )

Player = Character("Sagar", 80, 10, 50)
print(Player.status())