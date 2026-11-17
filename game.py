import random
from dungeon import Dungeon
from player import Player
from items import Weapon


class Game:
    def __init__(self):
        self.player = None
        self.dungeon = Dungeon()
        self.weapons = [
            Weapon("Iron Sword", bonus_damage=5, price=25),
            Weapon("Knight's Blade", bonus_damage=10, price=55),
        ]

    def run(self):
        self.show_intro()
        name = input("Enter your hero's name: ").strip() or "Hero"
        self.player = Player(name)

        while self.player.is_alive() and self.dungeon.room_number < self.dungeon.total_rooms:
            self.explore_room()

        if self.player.is_alive():
            print("\nYou conquered the dungeon. Victory!")
        else:
            print("\nGAME OVER. Your adventure ends here.")

        print("\nFinal character stats")
        print(self.player.status())

    def show_intro(self):
        print("=" * 46)
        print("          THE DUNGEON OF ASHES")
        print("=" * 46)
        print("Defeat enemies, collect rewards, and defeat the Dragon.")
        print("You have 3 health potions. Use them wisely.\n")

    def explore_room(self):
        enemy = self.dungeon.next_encounter()
        room = self.dungeon.room_number

        print("\n" + "=" * 46)
        print(f"ROOM {room}")
        print("=" * 46)
        if self.dungeon.is_final_room():
            print("The final boss appears!")
        else:
            print(f"A {enemy.name} blocks your path!")

        self.combat(enemy)

        if self.player.is_alive() and not self.dungeon.is_final_room():
            self.room_reward()

    def combat(self, enemy):
        while self.player.is_alive() and enemy.is_alive():
            print("\n" + "-" * 35)
            print(f"{self.player.name}: {self.player.health}/{self.player.max_health} HP")
            print(f"{enemy.name}: {enemy.health}/{enemy.max_health} HP")
            print("1. Attack")
            print("2. Use health potion")
            print("3. View character status")
            print("4. Run away")

            choice = input("Choose an action: ").strip()

            if choice == "1":
                self.player.attack(enemy)
            elif choice == "2":
                self.player.use_potion()
            elif choice == "3":
                print("\n" + self.player.status())
                continue
            elif choice == "4":
                if self.dungeon.is_final_room():
                    print("There is no escape from the final boss!")
                elif random.random() < 0.5:
                    print("You escaped the encounter.")
                    # Escaping counts as surviving the room but gives no reward.
                    enemy.health = 0
                    return
                else:
                    print("You failed to escape!")
            else:
                print("Please choose 1, 2, 3, or 4.")
                continue

            if enemy.is_alive() and self.player.is_alive():
                enemy.attack(self.player)

        if self.player.is_alive() and not enemy.is_alive():
            print(f"\nYou defeated {enemy.name}!")
            self.player.gain_xp(enemy.xp_reward)
            self.player.gold += enemy.gold_reward
            print(f"You found {enemy.gold_reward} gold.")

    def room_reward(self):
        print("\nYou find a quiet moment to prepare.")
        if random.random() < 0.5:
            self.player.potions += 1
            print("You found a health potion!")
        else:
            bonus_gold = random.randint(5, 15)
            self.player.gold += bonus_gold
            print(f"You found {bonus_gold} extra gold.")

        self.shop()

    def shop(self):
        print("\n--- Travelling Merchant ---")
        print(f"You have {self.player.gold} gold.")
        print("0. Leave shop")

        for index, weapon in enumerate(self.weapons, start=1):
            print(
                f"{index}. {weapon.name} "
                f"(+{weapon.bonus_damage} attack) - {weapon.price} gold"
            )

        choice = input("Buy an upgrade? ").strip()
        if choice == "0" or choice == "":
            return

        if not choice.isdigit():
            print("Please enter a number.")
            return

        item_index = int(choice) - 1
        if not 0 <= item_index < len(self.weapons):
            print("That item doesn't exist.")
            return

        weapon = self.weapons[item_index]
        if self.player.gold < weapon.price:
            print("You don't have enough gold.")
            return

        self.player.gold -= weapon.price
        self.player.attack_damage += weapon.bonus_damage
        print(f"You equipped {weapon.name}! Attack increased.")
