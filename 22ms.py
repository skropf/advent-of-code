#Millisecond 22
import os
from math import sqrt

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/22input.txt", 'r')

lines = file.read().strip().split('\n')

length = 1000
input_network = [['.' for x in range(length+len(lines))] for y in range(length+len(lines))]

to_insert = int(len(input_network) / 2) - int(len(lines) / 2)
for i in range(to_insert, to_insert+len(lines)):
    for j in range(to_insert, to_insert+len(lines)):
        input_network[i][j] = lines[i - to_insert][j - to_insert]

#Millisecond 22: First + Second half
dir = {"cur": [-1, 0], "up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

def clean():
    dir["cur"] = dir["up"]
    cur_pos = [int(len(input_network)/2), int(len(input_network)/2)]
    return (dir, cur_pos)

def turn(direction):
    if direction == "left":
        if dir["cur"] == dir["up"]: dir["cur"] = dir["left"]
        elif dir["cur"] == dir["down"]: dir["cur"] = dir["right"]
        elif dir["cur"] == dir["left"]: dir["cur"] = dir["down"]
        elif dir["cur"] == dir["right"]: dir["cur"] = dir["up"]
    if direction == "right":
        if dir["cur"] == dir["up"]: dir["cur"] = dir["right"]
        elif dir["cur"] == dir["down"]: dir["cur"] = dir["left"]
        elif dir["cur"] == dir["left"]: dir["cur"] = dir["up"]
        elif dir["cur"] == dir["right"]: dir["cur"] = dir["down"]
    if direction == "reverse":
        if dir["cur"] == dir["up"]: dir["cur"] = dir["down"]
        elif dir["cur"] == dir["down"]: dir["cur"] = dir["up"]
        elif dir["cur"] == dir["left"]: dir["cur"] = dir["right"]
        elif dir["cur"] == dir["right"]: dir["cur"] = dir["left"]

def scanning(network, bursts):
    (dir, cur_pos) = clean()
    infected = 0
    for burst in range(bursts):
        if network[cur_pos[0]][cur_pos[1]] == '#': #infected
            network[cur_pos[0]][cur_pos[1]] = '.'
            turn("right")

        elif network[cur_pos[0]][cur_pos[1]] == '.': #clean
            network[cur_pos[0]][cur_pos[1]] = '#'
            turn("left")
            infected += 1

        cur_pos = list(map(sum, zip(cur_pos, dir["cur"])))

    return infected

def advanced_scanning(network, bursts):
    (dir, cur_pos) = clean()
    infected = 0
    for burst in range(bursts):
        if network[cur_pos[0]][cur_pos[1]] == '#': #infected
            network[cur_pos[0]][cur_pos[1]] = 'F'
            turn("right")

        elif network[cur_pos[0]][cur_pos[1]] == '.': #clean
            network[cur_pos[0]][cur_pos[1]] = 'W'
            turn("left")

        elif network[cur_pos[0]][cur_pos[1]] == 'F': #flagged
            network[cur_pos[0]][cur_pos[1]] = '.'
            turn("reverse")

        elif network[cur_pos[0]][cur_pos[1]] == 'W': #weakened
            network[cur_pos[0]][cur_pos[1]] = '#'
            infected += 1


        cur_pos = list(map(sum, zip(cur_pos, dir["cur"])))

    return infected

import copy
network1 = copy.deepcopy(input_network)
network2 = copy.deepcopy(input_network)

print(scanning(network1, 10000))
print(advanced_scanning(network2, 10000000))
