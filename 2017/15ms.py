#Millisecond 15
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/15input.txt", 'r')

genA = int(file.readline().strip().split(' ')[-1])
genB = int(file.readline().strip().split(' ')[-1])

multiGenA = 16807
multiGenB = 48271

divisor = 2147483647

#Millisecond 15: First half
genA1 = genA
genB1 = genB
match = 0
for i in range(40000000):
    genA1 = genA1 * multiGenA % divisor
    genB1 = genB1 * multiGenB % divisor
    if genA1 & 0xffff == genB1 & 0xffff: match += 1

print(match)

#Millisecond 15: Second half
genA2 = genA
genB2 = genB
match = 0
comparison = 5000000
genA_list = []
genB_list = []
#first generating valid input lists
while len(genA_list) < 5000000 or len(genB_list) < 5000000:
    genA2 = genA2 * multiGenA % divisor
    genB2 = genB2 * multiGenB % divisor

    if genA2 % 4 == 0: genA_list.append(genA2)
    if genB2 % 8 == 0: genB_list.append(genB2)

for i in range(comparison):
    if genA_list[i] & 0xffff == genB_list[i] & 0xffff: match += 1

print(match)
