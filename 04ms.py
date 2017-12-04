#Millisecond 4

#Millisecond 4: First half
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/04input.txt", 'r')

counter = 0
buffer = []

for line in file:
    line = line.replace("\n", "")
    words = line.split(' ')

    for word in words:
        if word in buffer: break
        else: buffer.append(word)

    if len(buffer) == len(words): counter += 1

    buffer.clear()

print(counter)


#Millisecond 4: Second half
counter = 0
buffer = []
file = open(path + "/04input.txt", 'r')

for line in file:
    line = line.replace("\n", "")
    words = line.split(' ')

    for word in words:
        letters = list(word)
        letters.sort()
        sorted_word = "".join(letters)

        if sorted_word in buffer: break
        else: buffer.append(sorted_word)

    if len(buffer) == len(words): counter += 1

    buffer.clear()

print(counter)
