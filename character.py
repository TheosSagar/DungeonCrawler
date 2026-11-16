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
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_damage)
        print(f"{target.name} has {target.health} health remaining")

    def take_damage(self, damage):
        incoming_damage = damage
        actual_damage = max(0, incoming_damage - self.defence)
        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage")
        return self.health

class Player(Character):
    def __init__(self, name, health, attack_damage, defence, level, xp):
        super().__init__(name, health, attack_damage, defence)
        self.__level = 1
        self.__xp = 0

    def gain_xp(self, amount):
        self.xp += amount

    def show_progress(self):
        print(f"Players Level: {self.__level}, XP: {self.__xp}")

class Enemy(Character):
    def __init__(self, name, health, attack_damage, defence):
        super().__init__(name, health, attack_damage, defence)

class Dragon(Enemy):
    def __init__(self, name, health, attack_damage, defence):
        super().__init__(name, health, attack_damage, defence)

    def attack(self,target):
        print("Dragon unleased a powerfull attack!!!")
        target.take_damage(self.attack_damage)
        

player = Player("Sagar", 80, 20, 50, 1000, 1000000)
skeleton = Enemy("Skeleton", 30, 20, 10)
dragon = Dragon("Dragon", 100, 40, 20)

print(player.status())
print(skeleton.status())
print(dragon.status())

print("-------------------Attack-------------------")

skeleton.attack(player)
dragon.attack(player)

player.show_progress()
