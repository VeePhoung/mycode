import random

class DragonBallZCharacter:
    def __init__(self, name, hp, power_level, attack_damage, defense):
        self.name = name
        self.hp = hp
        self.power_level = power_level
        self.attack_damage = attack_damage
        self.defense = defense
        self.level = 1
        self.experience = 0
        self.max_hp = hp
        self.inventory = []

    def attack(self, enemy):
        damage = self.attack_damage * (self.power_level / enemy.defense)
        enemy.hp -= damage
        print(f"{self.name} attacks {enemy.name} for {damage:.2f} damage!")

    def defend(self, enemy):
        print(f"{self.name} defends against {enemy.name}'s attack.")

    def is_alive(self):
        return self.hp > 0

    def roll_dice(self):
        return random.randint(1, 20)

    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gains {exp} experience!")
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.power_level += 100
        self.attack_damage += 5
        self.defense += 2
        print(f"{self.name} levels up to level {self.level}!")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picks up {item}!")

# Define Dragon Ball Z characters
goku = DragonBallZCharacter("Goku", hp=100, power_level=9000, attack_damage=20, defense=10)
vegeta = DragonBallZCharacter("Vegeta", hp=90, power_level=8000, attack_damage=25, defense=12)
piccolo = DragonBallZCharacter("Piccolo", hp=80, power_level=7500, attack_damage=22, defense=15)

# Define enemies
enemies = [
    DragonBallZCharacter("Frieza", hp=200, power_level=10000, attack_damage=30, defense=20),
    DragonBallZCharacter("Cell", hp=250, power_level=12000, attack_damage=35, defense=25),
    DragonBallZCharacter("Majin Buu", hp=300, power_level=15000, attack_damage=40, defense=30)
]

# Define items
items = ["Senzu Bean", "Capsule Corp. Potion", "Z Sword"]

# Adventure function
def adventure(player):
    print(f"Welcome, {player.name}! Your adventure begins now.")
    while True:
        print("\n1. Travel to a new location")
        print("2. Train to level up")
        print("3. Pick up an item")
        print("4. Check inventory")
        print("5. Quit the game")
        choice = input("Enter your choice: ")

        if choice == "1":
            enemy = random.choice(enemies)
            print(f"\nYou encounter {enemy.name}!")
            while player.is_alive() and enemy.is_alive():
                player_roll = player.roll_dice()
                enemy_roll = enemy.roll_dice()
                print(f"{player.name} rolls a {player_roll}.")
                print(f"{enemy.name} rolls a {enemy_roll}.")
                if player_roll > enemy_roll:
                    player.attack(enemy)
                elif player_roll < enemy_roll:
                    enemy.attack(player)
                else:
                    print("It's a tie! No damage dealt.")
            if player.is_alive():
                player.gain_experience(50)
            else:
                print("You were defeated. Game over!")
                return
        elif choice == "2":
            player.level_up()
        elif choice == "3":
            item = random.choice(items)
            player.add_item(item)
        elif choice == "4":
            print("Inventory:")
            for item in player.inventory:
                print("-", item)
        elif choice == "5":
            print("Thanks for playing!")
            return
        else:
            print("Invalid choice. Try again.")

# Start the game
player_choice = input("Choose your character (Goku, Vegeta, Piccolo): ").capitalize()
if player_choice == "Goku":
    player = goku
elif player_choice == "Vegeta":
    player = vegeta
elif player_choice == "Piccolo":
    player = piccolo
else:
    print("Invalid character choice. Exiting game.")
    exit()

print(f"You have chosen {player.name}!")

# Start the adventure
adventure(player)

