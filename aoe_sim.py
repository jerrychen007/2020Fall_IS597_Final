import matplotlib.pyplot as plt
import pandas as pd
import math
import random

# FRANKS_PALADIN_HEALTH = 192
# PALADIN_HEALTH_WITH_BLOODLINES = 180
# PALADIN_HEALTH_WITHOUT_BLOODLINES = 160
INITIAL_ENEMY_NUMBER = 10
MAXIMUM_ENEMY_NUMBER = 100
DEFAULT_PALADIN_ATTACK = 18
DEFAULT_PALADIN_NORMAL_ARMOR = 5
DEFAULT_PALADIN_PIERCE_ARMOR = 7
Number_of_simulations = 500

soldiers_info = pd.read_csv('soldiers.csv')
col_to_list = soldiers_info['enemy_type'].tolist()
str = ', '.join(col_to_list)
print("We have these enemy types to select: "+ str)

# enemy_type = input("Enter the enemy type: ")
enemy_type = 'Hussar'

# def main():
#     simOneGame

def hits_to_kill(enemy_type, PALADIN_HEALTH):
    attack_type = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, "attack_type"].item()
    attack = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'attack'].item()
    health = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'health'].item()
    normal_armor = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'normal_armor'].item()
    pierce_armor = soldiers_info.loc[soldiers_info['enemy_type'] == enemy_type, 'pierce_armor'].item()
    if attack_type == 'normal':
        hits_can_take = PALADIN_HEALTH/(attack - DEFAULT_PALADIN_NORMAL_ARMOR)
        hits_to_kill_enemy = health/(DEFAULT_PALADIN_ATTACK - normal_armor)
    elif enemy_type.attack_type == 'pierce':
        hits_can_take = PALADIN_HEALTH/(attack - DEFAULT_PALADIN_PIERCE_ARMOR)
        hits_to_kill_enemy = health/(DEFAULT_PALADIN_ATTACK - normal_armor)
    hits_can_take = math.ceil(hits_can_take)
    hits_to_kill_enemy = math.ceil(hits_to_kill_enemy)
    return hits_can_take, hits_to_kill_enemy

def simNGames(Number_of_simulations, PALADIN_NUMBER, ENEMY_NUMBER, enemy_type, PALADIN_HEALTH):
    winsP = winsE = 0
    for i in range(Number_of_simulations):
        win = simOneGame(PALADIN_NUMBER, ENEMY_NUMBER, enemy_type, PALADIN_HEALTH)
        if win == 1:
            winsP = winsP + 1
        else:
            winsE = winsE + 1
    win_rate = winsP/Number_of_simulations
    return win_rate

def simOneGame(PALADIN_NUMBER, ENEMY_NUMBER, enemy_type, PALADIN_HEALTH):
    hits_can_take, hits_to_kill_enemy = hits_to_kill(enemy_type, PALADIN_HEALTH)
    p = {}
    e = {}
    for i in range(ENEMY_NUMBER):
        e[i] = hits_to_kill_enemy
    for i in range(PALADIN_NUMBER):
        p[i] = hits_can_take
    win = fight(p, e)
    return win

def fight(p, e):
    while checkwin(p, e) is False:
        paladin_targets = []
        enemies_targets = []
        for i in range(len(p.keys())):
            foes = list(e.keys())
            paladin_targets.append(random.choice(foes))
        for i in range(len(e.keys())):
            foes = list(p.keys())
            enemies_targets.append(random.choice(foes))
        for t in paladin_targets:
            e[t] = e[t]-1
        for t in enemies_targets:
            p[t] = p[t]-1
        p,e = checkdeath(p, e)
        if bool(p):
            win = 1
        else:
            win = 0
    return win

def checkdeath(p, e):
    if any(y <= 0 for y in p.values()):
        p = {x:y for x,y in p.items() if y>0}
    if any(y <= 0 for y in e.values()):
        e = {x:y for x,y in e.items() if y>0}
    return p, e

def checkwin(p, e):
    if bool(p) and bool(e):
        return False
    else:
        return True

# def draw_graph(resource_goal, num_villager_range: tuple = (5,30)):


win_rate = simNGames(Number_of_simulations, 40, 90, enemy_type, 192)
print(win_rate)
