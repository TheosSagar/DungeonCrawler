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

    def attack(self, target):
        target.take_damage(self.attack_damage)

    def take_damage(self, damage):
        incoming_damage = damage
        actual_damage = max(0, incoming_damage - self.defence)
        self.health -= actual_damage
        return self.health
        

player = Character("Sagar", 80, 20, 50)
skeleton = Character("Skeleton", 30, 20, 10)
dragon = Character("Dragon", 100, 40, 20)

print(player.status())
print(skeleton.status())
print(dragon.status())

print("-------------------Attack-------------------")

player.attack(skeleton)
print(player.status())
print(skeleton.status())