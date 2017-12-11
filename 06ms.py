#Millisecond 6
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/06input.txt", 'r')

input = []
for line in file:
    for mem_bank in line.split(' '):
        input.append(int(mem_bank.strip()))

def redistribute(buffer):
    #to save every state after redistribution
    states = []
    redistributions = 0

    while buffer not in states:
        states.append(buffer.copy())
        index = buffer.index(max(buffer))

        #save value to redistribute, set buffer at index to 0 and move to next element
        redistribution_count = buffer[index]
        buffer[index] = 0
        index += 1

        #run till there is nothing more to distribute
        while redistribution_count > 0:
            if index == len(buffer): index = 0

            buffer[index] += 1
            redistribution_count -= 1

            index += 1

        #increase the times of redistributions done
        redistributions += 1

    return (buffer, redistributions)


#Millisecond 6: First half
buffer = input.copy()
(buffer, redistributions) = redistribute(buffer)
print(redistributions)

#Millisecond 6: Second half (same code from first half just on old buffer)
(buffer, redistributions) = redistribute(buffer)
print(redistributions)
