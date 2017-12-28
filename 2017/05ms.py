#Millisecond 5
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/05input.txt", 'r')

input = []
for line in file:
    input.append(int(line.strip()))

#Millisecond 5: First half
steps = 0
index = 0
buffer = input.copy()
while index >= 0 and index < len(buffer):
    old_index = index
    index += buffer[index]
    buffer[old_index] += 1
    steps += 1

print(steps)

#Millisecond 5: Second half
steps = 0
index = 0
buffer = input.copy()
while index >= 0 and index < len(buffer):
    old_index = index
    index += buffer[old_index]
    if buffer[old_index] >= 3: buffer[old_index] -= 1
    else: buffer[old_index] += 1
    steps += 1

print(steps)
