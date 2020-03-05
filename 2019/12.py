### Day 12 - Part 1

puzzle_orig = open('12.input', 'r')

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


def read_input(puzzle_orig):
    puzzle_orig.seek(0)
    moons = []
    for line in puzzle_orig.readlines():
        line = line.strip()[1:-1].split(',')
        pos = []
        for p in line:
            pos.append(int(p.split('=')[1]))
        
        position = [pos[0], pos[1], pos[2]]

        moons.append(Moon(position))
    
    for moon in moons:
        for neighbour in moons:
            if moon != neighbour: moon.neighbours.append(neighbour)
    
    return moons

moons = read_input(puzzle_orig)

for i in range(1000):
    for moon in moons:
        moon.calc_velocity()
    for moon in moons:
        moon.apply_step()

print("Total energy:", sum([moon.total_energy() for moon in moons]))


### Day 12 - Part 2

moons = read_input(puzzle_orig)

prev_state_found = False
while not prev_state_found:
    
    # find a way to get find previous states


    for moon in moons:
        moon.calc_velocity()
    for moon in moons:
        moon.apply_step()

print("Universe is repeating itself after", len([]), "steps.")

