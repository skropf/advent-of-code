#Millisecond 14
import os
import numpy as np
from time import sleep

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/14input.txt", 'r')

key_string = file.read().strip()
key_strings = [key_string + "-" + str(x) for x in range(128)]

disk = [[None for _ in range(128)] for _ in range(128)]

#code from 10ms
def rotate(input):
    skip = 0
    position = 0
    hashlist = [x for x in range(256)]

    for i in range(64): #for second half
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



#Millisecond 14: First half
index = 0
for key in key_strings:
    input = [ord(x) for x in key]
    input.extend([17, 31, 73, 47, 23])
    hashlist = rotate(input)

    result = ""
    for chunk in np.array_split(hashlist, 16):
        xor = chunk[0]
        for elem in chunk[1:]:
            xor ^= elem
        result += "%0.2X" % xor

    buflist = []
    filler = ['.', '#']
    for hex in result:
        binary = bin(int(hex, 16))[2:].zfill(4)
        buflist.extend([filler[int(x)] for x in binary])

    disk[index] = buflist
    index += 1

squares_used = 0
for i in disk:
    for j in i:
        if j == '#':
            squares_used += 1

print(squares_used)

#Millisecond 14: Second half
def walk_disk(disk, x, y, region):
    if x < 0 or y < 0 or x > 127 or y > 127: return

    if disk[x][y] == '#':
        disk[x][y] = region
        walk_disk(disk, x+1, y, region)
        walk_disk(disk, x, y+1, region)
        walk_disk(disk, x-1, y, region)
        walk_disk(disk, x, y-1, region)


region = 0
for x in range(128):
    for y in range(128):
        if disk[x][y] == '#':
            walk_disk(disk, x, y, region)
            region += 1

print(region)
