from character import Character


class Enemy(Character):
    def __init__(self, name, health, attack_damage, defence, xp_reward, gold_reward):
        super().__init__(name, health, attack_damage, defence)
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 35, 13, 2, xp_reward=20, gold_reward=8)


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 45, 16, 3, xp_reward=25, gold_reward=12)


class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 120, 24, 6, xp_reward=100, gold_reward=60)

    def attack(self, target):
        if not self.is_alive() or not target.is_alive():
            return
        print("The Dragon unleashes a powerful flame attack!")
        target.take_damage(self.attack_damage)
