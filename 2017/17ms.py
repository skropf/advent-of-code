#Millisecond 17
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/17input.txt", 'r')

steps = int(file.read().strip())

#Millisecond 17: First half
repetition = 2017
vortex = [0]
cur_pos = 0

for x in range(1, repetition + 1):
    #setting current position and inserting into vortex
    cur_pos = (steps + cur_pos + 1) % len(vortex)
    vortex.insert(cur_pos, x)

print(vortex[vortex.index(2017) + 1])

#Millisecond 17: Second half
repetition = 50000000
cur_pos = 0
after_zero = -1

for i in range(1, repetition + 1):
    #setting current position
    cur_pos = (cur_pos + steps) % i
    
    if cur_pos == 0: after_zero = i

    #setting new current position with grown vortex
    cur_pos = (cur_pos + 1) % (i + 1)

print(after_zero)
