#Millisecond 8
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/08input.txt", 'r')


#Millisecond 8: First half + Second half
#init registry with all identifiers
registry = {}
for line in file:
    registry[line.split(' ')[0]] = 0

#reset file
file.seek(0)

#var for all-time maximum (=> second half)
maximum = 0
for line in file:
    elems = line.strip().split(' ')
    register = elems[0]
    operation = elems[1]
    value = int(elems[2])

    #creating expression for eval
    expression = str(registry[elems[4]]) + " " + elems[5] + " " + elems[6]

    #rechecking registry entry & evaluating condition
    if register in registry and eval(expression):
        if operation == "dec": registry[register] -= value
        if operation == "inc": registry[register] += value

    #setting all-time maximum
    if maximum < max(registry.values()): maximum = max(registry.values())

print(max(registry.values()))
print(maximum)
