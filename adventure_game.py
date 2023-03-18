import random
import time

# PLAYER CLASS #

class Player:
    level = 1
    experience = 0
    is_alive = True
    potions = 2

    def __init__(self, name, character_class):
        self.name = name
        if character_class.lower() == "warrior":
            self.character_class = character_class.title()
            self.strength = 5
            self.intelligence = 1
            self.cunning = 2
            self.max_health = 20
            self.current_health = 20
        elif character_class.lower() == "mage":
            self.character_class = character_class.title()
            self.strength = 2
            self.intelligence = 5
            self.cunning = 5
            self.max_health = 10
            self.current_health = 10
        elif character_class.lower() == "ranger":
            self.character_class = character_class.title()
            self.strength = 2
            self.intelligence = 3
            self.cunning = 5
            self.max_health = 15
            self.current_health = 15
        else:
            self.character_class = "Fish"
            self.strength = 1
            self.intelligence = 1
            self.cunning = 1
            self.max_health = 5
            self.current_health = 5

    def __repr__(self):
        return "{}, a level {} {}".format(self.name, self.level, self.character_class)

    def levelup(self):
        self.level += 1
        print("{} leveled up! {} is now level {}".format(self.name, self.name, self.level))
        self.strength *= 1.2
        self.intelligence *= 1.2
        self.cunning *= 1.2
        self.max_health += 2
        self.current_health = self.max_health
        print("Your stats are :-\nStrength: {:.1f}\nIntelligence: {:.1f}\nCunning: {:.1f}\nHealth: {:.1f}\n".format(self.strength, self.intelligence, self.cunning, self.max_health))

    def add_experience(self, experience):
        self.experience += experience
        print("{} gained {} experience points!".format(self.name, experience))
        if self.experience >= 50 + self.level * 50:
            self.levelup()
            self.experience = 0
        else:
            print("{} experience points to the next level\n".format((50 + self.level * 50) - self.experience))
    
    def attack(self, enemy):
        if type(enemy) == Enemy:
            hit = (self.strength + self.intelligence + self.cunning) * (random.randint(8, 12) * 0.1)
            print("{player_name} hit the enemy {enemy_name} for {hit:.1f} points\n".format(player_name = self.name, enemy_name = enemy.name, hit = hit))
            enemy.defend(hit)
  
    def defend(self, hit):
        self.current_health -= hit
        if (self.current_health <= 0):
            self.is_alive = False
            print("Oh no! {} was killed\n".format(self.name))
      
    def heal_up(self):
        if self.potions > 0:
            self.current_health += 10 + self.level * 2
            if self.current_health > self.max_health:
                self.current_health = self.max_health
            self.potions -= 1
            print("You healed 10 health points, you now have {:.1f} health and {} potions \n".format(self.current_health, self.potions))

# ENEMY CLASS #

class Enemy:
    is_alive = True
    name = "Slime"

    def __init__(self, player):
        if type(player) == Player:
            self.level = random.randint(1, player.level)
            self.strength = self.level * random.randint(1, 2)
            self.intelligence = self.level * random.randint(1, 2)
            self.cunning = self.level * random.randint(1, 2)
            self.health = self.level * random.randint(5, 10)
            self.experience = self.level * 50

    def __repr__(self):
        return "A level {} {} with {} health points".format(self.level, self.name, self.health)

    def attack(self, player):
        if type(player) == Player:
            hit = (self.strength + self.intelligence + self.cunning) * (random.randint(3, 8) * 0.1)
            print("Enemy {enemy_name} hit {player_name} for {hit:.1f} points".format(player_name = player.name, enemy_name = self.name, hit = hit))
            player.defend(hit)
  
    def defend(self, hit):
        self.health -= hit
        if (self.health <= 0):
            self.is_alive = False
            print("The enemy {} was killed!".format(self.name))

# MAIN PROGRAM #
print("Welcome to Adventure Killing Floor!")
name = input("Enter player name: ")
player_class = input("Enter your class: ")
if player_class.lower() != "warrior" and player_class.lower() != "ranger" and player_class.lower() != "mage":
    print("Thats not a real class! As punishment you shall be a fish!")

player = Player(name, player_class)
print("Congratulations, you have created {}".format(player))
print("Your stats are :-\nStrength: {:.1f}\nIntelligence: {:.1f}\nCunning: {:.1f}\nHealth: {:.1f}\n".format(player.strength, player.intelligence, player.cunning, player.max_health))

while player.is_alive == True:
    enemy = Enemy(player)
    print("{} has spawned! {} must defend themselves!".format(enemy, player.name))
    while enemy.is_alive == True:
        print("You currently have {:.1f} health points\n".format(player.current_health))
        option = input("Do you want to attack or heal ({} potions available)? ".format(player.potions))
        if option.lower() == "attack":
            player.attack(enemy)
        elif option.lower() == "heal":
            player.heal_up()
            
        if enemy.is_alive:
            enemy.attack(player)
        else:
            player.add_experience(enemy.experience)
            player.potions += random.randint(0, 1)
            break
        if player.is_alive == False:
            break
      
print("You reached level {} with {} {}".format(player.level, player.character_class, player.name))
print("Please play again soon!")
