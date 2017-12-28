#Millisecond 1
import os

path = os.path.dirname(os.path.realpath(__file__))
input = open(path + "/01input.txt", 'r').read()

#Millisecond 1: First half
sum = 0
for i in range(len(input)):
    if i+1 < len(input):
        if input[i] == input[i + 1]: sum += int(input[i])
    else:
        if input[i] == input[0]: sum += int(input[i])
print("Sum pairs: " + str(sum))

#Millisecond 1: Second half
sum = 0
step = int(len(input) / 2)
for i in range(len(input)):
    if i+step < len(input):
        if input[i] == input[i + step]: sum += int(input[i])
    else:
        if input[i] == input[i + step - len(input)]: sum += int(input[i])
print("Sum + Half-list step: " + str(sum))
