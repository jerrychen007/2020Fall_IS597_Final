# All data are gathered from the latest version of Age of Empires II: Definitive Edition (https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/)

class Champion:
    def __init__(self):
        self.attack_type = 'normal'
        self.health = 70
        self.attack = 17
        self.normal_armor = 4
        self.pierce_armor = 5

class Halberdier:
    def __init__(self):
        self.attack_type = 'normal'
        self.health = 60
        self.attack = 42
        self.normal_armor = 3
        self.pierce_armor = 4

class Paladin:
    def __init__(self):
        self.attack_type = 'normal'
        self.health = 180
        self.attack = 18
        self.normal_armor = 5
        self.pierce_armor = 7

class Elite_War_Elephant:
    def __init__(self):
        self.attack_type = 'normal'
        self.health = 620
        self.attack = 24
        self.normal_armor = 4
        self.pierce_armor = 7

class Hussar:
    def __init__(self):
        self.attack_type = 'normal'
        self.health = 95
        self.attack = 11
        self.normal_armor = 3
        self.pierce_armor = 6

class Arbalester:
    def __init__(self):
        self.attack_type = 'pierce'
        self.health = 40
        self.attack = 10
        self.normal_armor = 3
        self.pierce_armor = 4

class Hand_Cannoneer:
    def __init__(self):
        self.attack_type = 'pierce'
        self.health = 35
        self.attack = 17
        self.normal_armor = 4
        self.pierce_armor = 4

class Heavy_Cavalry_Archer:
    def __init__(self):
        self.attack_type = 'pierce'
        self.health = 80
        self.attack = 11
        self.normal_armor = 5
        self.pierce_armor = 6
