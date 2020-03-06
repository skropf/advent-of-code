### Day 12 - Part 1

class Moon(object):
    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]
        self.neighbours = []
    
    def calc_velocity(self):
        for moon in self.neighbours:
            if moon.position[0] > self.position[0]: self.velocity[0] += 1
            elif moon.position[0] < self.position[0]: self.velocity[0] -= 1
            if moon.position[1] > self.position[1]: self.velocity[1] += 1
            elif moon.position[1] < self.position[1]: self.velocity[1] -= 1
            if moon.position[2] > self.position[2]: self.velocity[2] += 1
            elif moon.position[2] < self.position[2]: self.velocity[2] -= 1

    def apply_step(self):
        self.position = [x+y for x,y in zip(self.position, self.velocity)]
    
    def pot_energy(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kin_energy(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def total_energy(self):
        return self.pot_energy() * self.kin_energy()
    
    def __repr__(self):
        return "pos=<x="+str(self.position[0])+", y="+str(self.position[1])+", z="+str(self.position[2])+">, vel=<x="+str(self.velocity[0])+", y="+str(self.velocity[1])+", z="+str(self.velocity[2])+">"

def read_input():
    puzzle_orig = open('12.input', 'r')

    moons = []
    for line in puzzle_orig.readlines():
        line = line.strip()[1:-1].split(',')
        position = []
        for p in line:
            position.append(int(p.split('=')[1]))
        
        moons.append(Moon(position))
    
    puzzle_orig.close()

    for moon in moons:
        for neighbour in moons:
            if moon != neighbour: moon.neighbours.append(neighbour)
    
    return moons

moons = read_input()

for i in range(1000):
    for moon in moons:
        moon.calc_velocity()
    for moon in moons:
        moon.apply_step()

print("Total energy:", sum([moon.total_energy() for moon in moons]))

### Day 12 - Part 2

from math import gcd
from itertools import combinations

# lowest common multiple
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

moons = read_input()

starting_positions = [moon.position for moon in moons]
x_found, y_found, z_found = False, False, False
# different from the first part, the initial state already counts => i = 1
i = 1
while not x_found or not y_found or not z_found:
    for moon in moons: moon.calc_velocity()
    for moon in moons: moon.apply_step()
    current_positions = [moon.position for moon in moons]

    i += 1

    if [c[0] for c in current_positions] == [s[0] for s in starting_positions] and not x_found: x_found = i
    if [c[1] for c in current_positions] == [s[1] for s in starting_positions] and not y_found: y_found = i
    if [c[2] for c in current_positions] == [s[2] for s in starting_positions] and not z_found: z_found = i

print("Universe is repeating itself after", lcm(lcm(x_found, y_found), z_found), "steps.")

