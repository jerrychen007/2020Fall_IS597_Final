import matplotlib.pyplot as plt
import pandas as pd
import math

DEFAULT_FRANKS_PALADIN_HEALTH = 192
DEFAULT_PALADIN_HEALTH = 160
INITIAL_PALADIN_NUMBER = 40
INITIAL_ENEMY_NUMBER = 40
DEFAULT_PALADIN_ATTACK = 18
DEFAULT_PALADIN_NORMAL_ARMOR = 5
DEFAULT_PALADIN_PIERCE_ARMOR = 7
Number_of_simulations = 100

soldiers_info = pd.read_csv('soldiers.csv')
col_to_list = soldiers_info['enemy_type'].tolist()
str = ', '.join(col_to_list)
print("We have these enemy types to select: "+ str)

enemy_type = input("Enter the enemy type: ")

def main():


def hits_can_take(enemy_type):
    attack_type = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, "attack_type"].item()
    attack = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'attack'].item()
    health = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'health'].item()
    normal_armor = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'normal_armor'].item()
    pierce_armor = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'pierce_armor'].item()
    if attack_type == 'normal':
        hits_can_take = DEFAULT_FRANKS_PALADIN_HEALTH/(attack - DEFAULT_PALADIN_NORMAL_ARMOR)
        hits_to_kill_enemy = health/(DEFAULT_PALADIN_ATTACK - normal_armor)
    elif enemy_type.attack_type == 'pierce':
        hits_can_take = DEFAULT_FRANKS_PALADIN_HEALTH/(attack - DEFAULT_PALADIN_PIERCE_ARMOR)
        hits_to_kill_enemy = health/(DEFAULT_PALADIN_ATTACK - normal_armor)
    hits_can_take = math.ceil(hits_can_take)
    hits_to_kill_enemy = math.ceil(hits_to_kill_enemy)
    return hits_can_take, hits_to_kill_enemy

def battle_end(battlefield):
    for key in battlefield.keys():
        if battlefield[key] != 0:
            return False
    return True

def draw_graph(resource_goal, num_villager_range: tuple = (5,30)):
    def generate_graph_title():
        begin = 'The time of generating '
        temp_list = []
        for key in resource_goal:
            if resource_goal[key] != 0:
                temp_list.append( str(resource_goal[key]) + ' ' + key)
        return begin + ','.join(temp_list)

    low, high = num_villager_range
    success_rates = []
    for n_villager in range(low, high + 1):
        sim1 = AoeSimulator()
        sim1.set_resource_goal(resource_goal)
        time_took = sim1.complex_sim(n_villager, return_value=True)
        time_list.append(time_took)

    plt.title(generate_graph_title())
    plt.xlabel('Number of Enemies')
    plt.ylabel('Success rate')
    plt.plot(range(low, high + 1), success_rates)
    plt.show()

if __name__ == '__main__':
    min_enemy = 10
    max_enemy = 100
