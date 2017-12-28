
#Millisecond 21
import os
from math import sqrt

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/21input.txt", 'r')

lines = file.read().strip().split('\n')

rules = {}
for line in lines:
    elems = line.split(" => ")
    rules[elems[0]] = elems[1]

starting_pattern = ".#./..#/###".split('/')

#Millisecond 21: First half
def transform(pattern, type):
    if type == "rotate":
        result = zip(*pattern[::-1])
        return list("".join(x) for x in list(result))

    if type == "flip":
        return list("".join(reversed(x)) for x in pattern)

def get_all_transformations(pattern):
    transformations = []
    transformations.append(pattern)
    transformations.append(transform(transformations[0], "rotate"))
    transformations.append(transform(transformations[1], "rotate"))
    transformations.append(transform(transformations[2], "rotate"))

    transformations.append(transform(pattern, "flip"))
    transformations.append(transform(transformations[4], "rotate"))
    transformations.append(transform(transformations[5], "rotate"))
    transformations.append(transform(transformations[6], "rotate"))

    return transformations

def get_rule(pattern):
    transformations = get_all_transformations(pattern)
    for p in transformations:
        rule_key = '/'.join(p)
        if rule_key in rules:
            return rules[rule_key].split('/')

def divide_pattern(starting_pattern):
    if len(starting_pattern) % 2 == 0:
        for i in range(0, len(starting_pattern), 2):
            for j in range(0, len(starting_pattern), 2):
                pattern = [starting_pattern[i][j:j+2], starting_pattern[i+1][j:j+2]]
                yield pattern
    else: #len(starting_pattern) % 3 == 0
        for i in range(0, len(starting_pattern), 3):
            for j in range(0, len(starting_pattern), 3):
                pattern = [starting_pattern[i][j:j+3], starting_pattern[i+1][j:j+3], starting_pattern[i+2][j:j+3]]
                yield pattern

def enhance(starting_pattern):
    enhanced = []
    for pattern in divide_pattern(starting_pattern):
        enhanced.append(get_rule(pattern))

    pattern = ""
    row_length = len(enhanced[0])
    column_length = int(sqrt(len(enhanced)))
    finished_pattern = []

    for column_big in range(0, len(enhanced), column_length):
        for row in range(row_length):
            for column_small in range(column_length):
                pattern += enhanced[column_big+column_small][row]
            finished_pattern.append(pattern)
            pattern = ""

    return finished_pattern

pattern = starting_pattern
for i in range(5): pattern = enhance(pattern)
print("/".join(pattern).count('#'))

#Millisecond 21: Second half
pattern = starting_pattern
for i in range(18): pattern = enhance(pattern)
print("/".join(pattern).count('#'))
