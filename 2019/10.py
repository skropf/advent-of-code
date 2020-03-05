### Day 10 - Part 1

from math import atan2, pi

puzzle_orig = open('10.input', 'r')
space_map = [[y for y in x.strip()] for x in puzzle_orig.readlines()]

# put all asteroids in list
astroids = []
for i in range(len(space_map)):
    for j in range(len(space_map)):
        if space_map[j][i] == '#':
            astroids.append((i, j))

# calculate angles from one asteroid to all others and check how many we can see
max_astroid_views = 0
best_position = None
astroids_positions = {}
for origin in astroids:
    angles = {(ax, ay): atan2(ay - origin[1], ax - origin[0]) for ax, ay in astroids}
    # remove itself from list
    del(angles[origin])
    astroids_seen = {}
    for a in astroids:
        if a in angles and angles[a] not in astroids_seen.values():
            astroids_seen[a] = angles[a]
    if len(astroids_seen) > max_astroid_views:
        best_position = origin
        max_astroid_views = len(astroids_seen)
        astroids_positions = astroids_seen

print("The best place for a monitoring station is", best_position, "with", max_astroid_views, "asteroids in view.")

### Day 10 - Part 2

# sorting astroids by angle
astroids_positions = {pos: angle for pos, angle in sorted(astroids_positions.items(), key=lambda angle: angle[1])}

# -pi/2 is straight up - therefore finding index of first shot astroid
start_index = None
for astroid in astroids_positions.items():
    if astroid[1] >= -pi/2:
        start_index = list(astroids_positions.keys()).index(astroid[0])
        break

# calculating index of the 200th astroid shot. -1 because start_index itself counts too
final_index = None
if start_index+200 > len(astroids_positions): final_index = start_index + 200 - len(astroids_positions) - 1
else: final_index = start_index + 200 - 1

print("The 200th astroid shot is at position:", list(astroids_positions.keys())[final_index])