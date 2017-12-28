#Millisecond 10
import os
from numpy import array_split


path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/10input.txt", 'r')

#creating inputs for first and second part
input1 = [int(x) for x in file.read().strip().split(',')]
file.seek(0)
input2 = [ord(x) for x in file.read().strip()]
input2.extend([17, 31, 73, 47, 23])


#function for reversing the specified length of the hashlist and reinserting it
def rotate(input, repeat=1):
    skip = 0
    position = 0
    hashlist = [x for x in range(256)]

    for i in range(repeat): #for second half
        for length in input:
            sublist = []

            #save old position and move the specified length into sublist
            position_old = position
            for i in range(length):
                sublist.append(hashlist[position % 256])
                position += 1

            #reversing sublist
            sublist = list(reversed(sublist))

            #reposition and reinsert sublist
            position = position_old
            for elem in sublist:
                hashlist[position % 256] = elem
                position += 1

            #set new position and increase skip
            position += skip
            position %= len(hashlist)
            skip += 1

    return hashlist

#Millisecond 10: First half
hashlist = rotate(input1)
print(hashlist[0] * hashlist[1])

#Millisecond 10: Second half
hashlist = rotate(input2, 64)
result = ""

#split hashlist into 16x16 chunks, xor all elems of each chunk and
#concatenate the xor results
for chunk in array_split(hashlist, 16):
    xor = chunk[0]
    for elem in chunk[1:]:
        xor ^= elem
    result += "%0.2X" % xor

print(result)
