from character import Character


class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_damage=18, defence=5)
        self.__level = 1
        self.__xp = 0
        self.__xp_to_next_level = 50
        self.potions = 3
        self.gold = 0

    @property
    def level(self):
        return self.__level

    @property
    def xp(self):
        return self.__xp

    def gain_xp(self, amount):
        self.__xp += amount
        print(f"{self.name} gained {amount} XP!")

        while self.__xp >= self.__xp_to_next_level:
            self.__xp -= self.__xp_to_next_level
            self.level_up()

    def level_up(self):
        self.__level += 1
        self.__xp_to_next_level = int(self.__xp_to_next_level * 1.5)
        self.max_health += 15
        self.health = self.max_health
        self.attack_damage += 3
        self.defence += 1

        print("\n*** LEVEL UP! ***")
        print(f"You are now level {self.__level}!")
        print("Your health, attack and defence have increased.")
        print("Your health has been fully restored.")

    def use_potion(self):
        if self.potions <= 0:
            print("You don't have any potions.")
            return

        if self.health == self.max_health:
            print("Your health is already full.")
            return

        self.potions -= 1
        self.heal(35)
        print(f"Potions remaining: {self.potions}")

    def show_progress(self):
        print(
            f"{self.name} | Level {self.__level} | "
            f"XP {self.__xp}/{self.__xp_to_next_level} | Gold: {self.gold}"
        )

    def status(self):
        return (
            super().status()
            + f"\nLevel: {self.__level}"
            + f"\nXP: {self.__xp}/{self.__xp_to_next_level}"
            + f"\nPotions: {self.potions}"
            + f"\nGold: {self.gold}"
        )
