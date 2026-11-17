class Character:
    """Base class shared by the player and all enemies."""

    def __init__(self, name, health, attack_damage, defence):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_damage = attack_damage
        self.defence = defence

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defence)
        self.health = max(0, self.health - actual_damage)
        print(f"{self.name} takes {actual_damage} damage.")

        if not self.is_alive():
            print(f"{self.name} has been defeated!")

        return actual_damage

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because they are defeated.")
            return

        if not target.is_alive():
            print(f"{target.name} is already defeated.")
            return

        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_damage)

    def heal(self, amount):
        if not self.is_alive():
            print(f"{self.name} cannot be healed because they are defeated.")
            return 0

        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        healed = self.health - old_health
        print(f"{self.name} restores {healed} HP.")
        return healed

    def status(self):
        return (
            f"{self.name}\n"
            f"HP: {self.health}/{self.max_health}\n"
            f"Attack: {self.attack_damage}\n"
            f"Defence: {self.defence}"
        )
