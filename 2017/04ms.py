#Millisecond 4

#Millisecond 4: First half
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/04input.txt", 'r')

input = []
for line in file:
    input.append(line.replace("\n", "").split(' '))

counter = 0
buffer = []
for words in input:
    for word in words:
        if word in buffer: break
        else: buffer.append(word)

    if len(buffer) == len(words): counter += 1

    buffer.clear()

print(counter)


#Millisecond 4: Second half
counter = 0
buffer = []
for words in input:
    for word in words:
        letters = list(word)
        letters.sort()
        sorted_word = "".join(letters)

        if sorted_word in buffer: break
        else: buffer.append(sorted_word)

    if len(buffer) == len(words): counter += 1

    buffer.clear()

print(counter)
