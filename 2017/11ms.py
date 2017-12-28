#Millisecond 10
import os


path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/11input.txt", 'r')

input = [x for x in file.read().strip().split(',')]

farthest = 0
steps = 0
dir = {"x": 0, "y": 0, "z": 0}

#converting
#flat hexagon cardinal direction coord.-system to
#pointy hexagon kartesic coord.-system
for d in input:
    if d == "n":
        dir["x"] += 1
        dir["z"] += 1
    if d == "ne":
        dir["x"] += 1
        dir["y"] += 1
    if d == "se":
        dir["y"] += 1
        dir["z"] -= 1
    if d == "s":
        dir["x"] -= 1
        dir["z"] -= 1
    if d == "sw":
        dir["x"] -= 1
        dir["y"] -= 1
    if d == "nw":
        dir["y"] -= 1
        dir["z"] += 1

    steps = int((abs(dir["x"]) + abs(dir["y"]) + abs(dir["z"])) / 2)
    if steps > farthest: farthest = steps

print(steps)
print(farthest)
