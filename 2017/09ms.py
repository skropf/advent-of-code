#Millisecond 9
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/09input.txt", 'r')

input = file.read()

open_groups = []

def addup_score(input):
    i, score, count_garbage = (0, 0, 0)
    while i < len(input):
        char = input[i]

        #update nesting and calculating score
        if char is "{":
            open_groups.append(char)
            score += len(open_groups)
        if char is "}": open_groups.pop()

        #garbage ignore everything until it closes + Second half: count garbage chars
        if char == "<":
            i += 1
            while i < len(input):
                garbage = input[i]
                if garbage == ">": break
                if garbage == "!": i += 2
                else:
                    count_garbage += 1
                    i += 1

        i += 1

    return (score, count_garbage)

(score, count_garbage) = addup_score(input)
print(score)
print(count_garbage)
