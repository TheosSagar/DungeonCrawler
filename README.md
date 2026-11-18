# The Dungeon of Ashes — Python OOP CLI RPG

A small turn-based dungeon crawler built with Python's standard library.
No external packages are required.

This project was done to learn OOP in python.

## Run the game

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python main.py
   ```

On Windows, `py main.py` also works.

## Project structure

```text
dungeon_crawler_rpg/
├── main.py        # Program entry point
├── game.py        # Main game loop, combat flow, shop and rewards
├── character.py  # Base Character class
├── player.py     # Player stats, XP, levels and potions
├── enemy.py      # Enemy base class and enemy types
├── items.py      # Item, Potion and Weapon classes
├── dungeon.py    # Room progression and enemy encounters
└── README.md
```

## OOP concepts to study

- **Classes and objects:** `Player()`, `Skeleton()`, `Dragon()`
- **Inheritance:** `Player` and `Enemy` inherit from `Character`; enemy types inherit from `Enemy`.
- **Encapsulation:** `Player` stores XP and level in `__xp` and `__level`.
- **Polymorphism:** `Dragon.attack()` overrides `Character.attack()`.
- **Composition:** `Game` owns a `Player` and a `Dungeon`; the game uses item and enemy objects.
- **Methods and state:** health, gold, potions, room number and XP change as the game runs.

## Suggested learning order

Do not try to understand every file at once. Read and run in this order:

1. `character.py` — understand the common character behaviour.
2. `player.py` — study `super()`, private attributes, properties and levelling.
3. `enemy.py` — compare inheritance and method overriding.
4. `items.py` — understand small reusable classes.
5. `dungeon.py` — understand random encounters and game state.
6. `game.py` — follow the complete game loop and combat flow.
7. `main.py` — understand how the application starts.

## Game rules

- Clear five rooms. The fifth room contains the Dragon.
- Defeat enemies to earn XP and gold.
- Level up to improve your stats.
- Use health potions during combat.
- Spend gold on permanent weapon attack upgrades.
- You can try to escape regular encounters, but escaping gives no reward.
