#Millisecond 10
import os
from numpy import array_split


path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/10input.txt", 'r')

input1 = [int(x) for x in file.read().strip().split(',')]
file.seek(0)
input2 = [ord(x) for x in file.read().strip()]
input2.extend([17, 31, 73, 47, 23])

def rotate(input, repeat=1):
    skip = 0
    position = 0
    hash = [x for x in range(256)]

    for i in range(repeat): #for second half
        for length in input:
            sublist = []

            position_old = position
            for i in range(length):
                sublist.append(hash[position % 256])
                position += 1

            sublist = list(reversed(sublist))

            position = position_old
            for elem in sublist:
                hash[position % 256] = elem
                position += 1

            position += skip
            skip += 1
            position %= len(hash)

    return hash

#Millisecond 10: First half
hash = rotate(input1)
print(hash[0] * hash[1])

#Millisecond 10: Second half
hash = rotate(input2, 64)
result = ""

for chunk in array_split(hash, 16):
    xor = chunk[0]
    for elem in chunk[1:]:
        xor ^= elem
    result += "%0.2X" % xor

print(result)
