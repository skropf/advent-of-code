#Millisecond 6
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/06input.txt", 'r')

input = []
for line in file:
    for mem_bank in line.split(' '):
        mem_bank = int(mem_bank.strip())
        input.append(mem_bank)

#Millisecond 6: First half
states = []
buffer = input.copy()
redistributions = 0
while buffer not in states:
    states.append(buffer.copy())
    index = buffer.index(max(buffer))

    redistribution_count = buffer[index]
    buffer[index] = 0
    index += 1
    while redistribution_count > 0:
        if index == len(buffer): index = 0

        buffer[index] += 1
        redistribution_count -= 1

        index += 1

    redistributions += 1

print(redistributions)

#Millisecond 6: Second half (same code from first half just on old buffer)
states = []
redistributions = 0
while buffer not in states:
    states.append(buffer.copy())
    index = buffer.index(max(buffer))

    redistribution_count = buffer[index]
    buffer[index] = 0
    index += 1
    while redistribution_count > 0:
        if index == len(buffer): index = 0

        buffer[index] += 1
        redistribution_count -= 1

        index += 1

    redistributions += 1


print(redistributions)
