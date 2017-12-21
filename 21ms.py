
#Millisecond 21
import os
from math import sqrt

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/21input.txt", 'r')

lines = file.read().strip().replace('#', '1').replace('.', '0').split('\n')

rules = {}
for line in lines:
    elems = line.split(" => ")
    rules[elems[0]] = elems[1]

starting_pattern = ".#./..#/###".replace('#', '1').replace('.', '0').split('/')


#Millisecond 21: First half
def transform(pattern, type):
    if len(pattern) == 2:
        if type == "h_flip":
            return [pattern[1], pattern[0]]
        if type == "v_flip":
            return [pattern[0][::-1], pattern[1][::-1]]
        if type == "rotate":
            return [pattern[1][0] + pattern[0][0],
                    pattern[1][1] + pattern[0][1]]

    if len(pattern) == 3:
        if type == "h_flip":
            return [pattern[2], pattern[1], pattern[0]]
        if type == "v_flip":
            return [pattern[0][::-1], pattern[1][::-1], pattern[2][::-1]]
        if type == "rotate":
            return [pattern[2][0] + pattern[1][0] + pattern[0][0],
                    pattern[2][1] + pattern[1][1] + pattern[0][1],
                    pattern[2][2] + pattern[1][2] + pattern[0][2]]

def get_all_transformations(pattern):
    rot0 = pattern
    rot90 = transform(rot0, "rotate")
    rot180 = transform(rot90, "rotate")
    rot270 = transform(rot180, "rotate")

    flip_h = transform(pattern, "h_flip")
    flip_v = transform(pattern, "v_flip")

    flip_h_rot = transform(flip_h, "rotate")
    flip_v_rot = transform(flip_v, "rotate")

    yield rot0
    yield rot90
    yield rot180
    yield rot270
    yield flip_h
    yield flip_v
    yield flip_h_rot
    yield flip_v_rot

def get_rule(pattern):
    for p in get_all_transformations(pattern):
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
print("/".join(pattern).count('1'))

#Millisecond 21: Second half
pattern = starting_pattern
for i in range(18): pattern = enhance(pattern)
print("/".join(pattern).count('1'))
