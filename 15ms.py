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
match = 0
for i in range(40000000):
    genA = genA * multiGenA % divisor
    genB = genB * multiGenB % divisor

    lenA = len(str(bin(genA)))
    lenB = len(str(bin(genB)))

    if bin(genA)[lenA-16:lenA] == bin(genB)[lenB-16:lenB]: match += 1

print(match)

#Millisecond 15: Second half
match = 0
genA_list = []
genB_list = []
#first generating valid input lists
while len(genA_list) < 5000000 or len(genB_list) < 5000000:
    genA = genA * multiGenA % divisor
    genB = genB * multiGenB % divisor

    if genA % 4 == 0: genA_list.append(genA)
    if genB % 8 == 0: genB_list.append(genB)

#validating generated inputs
for genA, genB in zip(genA_list, genB_list):
    binA = bin(genA)
    binB = bin(genB)

    lenA = len(str(binA))
    lenB = len(str(binB))

    if binA[lenA-16:lenA] == binB[lenB-16:lenB]: match += 1

    i += 1

print(match)
