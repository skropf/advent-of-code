from itertools import permutations

import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/02input.txt", 'r')

input = []
for line in file:
    input.append([int(x) for x in line.strip().replace('\t', ' ').split(' ')])

#Millisecond 2

#Millisecond 2: First half
checksum = 0
for line in input:
    maxi = max(line)
    mini = min(line)

    checksum += (maxi - mini)

print(checksum)

#Millisecond 2: Second half
checksum = 0
for line in input:
    possibilities = permutations(line, 2)
    for possibility in possibilities:
        maxi = max(possibility)
        mini = min(possibility)


        if maxi % mini == 0:
            checksum += maxi / mini

#half the checksum because it will calculate both permutations (e.g. (12,4) and (4,12))
print(checksum / 2)
