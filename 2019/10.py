### Day 10 - Part 1

from copy import deepcopy
from itertools import permutations
from math import gcd

puzzle_orig = open('10.input', 'r')
asteroid_map = [[y for y in x.strip()] for x in puzzle_orig.readlines()]
size = len(asteroid_map)

# generate all possible view vectors in this 2D space
vectors = permutations(range(-size, size), 2)


print(sorted(vectors))




def count_viewable_asteroids(position, asteroid_map, view_vectors):
    viewable_asteroids = 0
    asteroid_map[position[1]][position[0]] = 'H'

    for view in view_vectors:
        x = view[0]
        y = view[1]

        while 0 < position[1] + y < size and 0 < position[0] + x < size:
            
            if asteroid_map[position[1] + y][position[0] + x] == '#':
                asteroid_map[position[1] + y][position[0] + x] = 's'
                viewable_asteroids += 1
                break
            else:
                x += view[0]
                y += view[1]
    
    return viewable_asteroids

max_asteroid_views, best_position, best_map = 0, (), []
for i in range(size):
    for j in range(size):
        if asteroid_map[j][i] == '#':
            cur_map = deepcopy(asteroid_map)
            asteroid_views = count_viewable_asteroids((i, j), cur_map, vectors)

            if asteroid_views > max_asteroid_views:
                max_asteroid_views = asteroid_views
                best_position = (i, j)
                best_map = cur_map


print("The best place for a monitoring station is", best_position, "with", max_asteroid_views, "asteroids in view.")
for line in best_map:
    print(line)