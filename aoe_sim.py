import soldiers
import matplotlib.pyplot as plt

DEFAULT_FRANKS_PALADIN_HEALTH = 192  # as per game start
DEFAULT_PALADIN_HEALTH = 180
DEFAULT_PALADIN_NUMBER = 40
DEFAULT_PALADIN_ATTACK = 18
DEFAULT_PALADIN_NORMAL_ARMOR = 5
DEFAULT_PALADIN_PIERCE_ARMOR = 7
DEFAULT_ENEMY_ATTACK = 10
UPGRADE_COSTS_GOLD = 1050
Number_of_simulations = 100

class AoeIISimulator:
    def __init__(self, Paladins = DEFAULT_PALADIN_NUMBER):
        self.Paladins = Paladins
        self.enemy_attack = DEFAULT_ENEMY_ATTACK

    def hits_can_take(self, attack_type):
        if attack_type == 'normal':
            hits_can_take = health/(enemy_attack - normal_armor)
        elif attack_type == 'pierce':
            hits_can_take = enemy_attack - normal_armor



    def battle_end(self):
        for key in self.armies.keys():
            if self.armies[key] != 0:
                return False
        return True

    def draw_graph(self):



if __name__ == '__main__':

    min_enemy_soldiers = 10
    max_enemy_soldiers = 100
    goal = {'Paladins': 0} or {'Enemy_soldiers': 0}

    sim = AoeIISimulator()
    sim.draw_graph(goal, (min_enemy_soldiers, max_enemy_soldiers))

