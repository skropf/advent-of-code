#Millisecond 20
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/20input.txt", 'r')

lines = file.read().strip().split('\n')


#feed the input
i = 0
particles = {}
for line in lines:
    elems = line.split(', ')

    position = [int(x) for x in elems[0].split('=')[1].replace('<', '').replace('>', '').split(',')]
    velocity = [int(x) for x in elems[1].split('=')[1].replace('<', '').replace('>', '').split(',')]
    acceleration = [int(x) for x in elems[2].split('=')[1].replace('<', '').replace('>', '').split(',')]

    particles[i] = {"px": position[0], "py": position[1], "pz": position[2], "vx":velocity[0], "vy":velocity[1], "vz":velocity[2], "ax":acceleration[0], "ay":acceleration[1], "az":acceleration[2]}
    i += 1


#Millisecond 20: First half
def accel(key): return abs(particles[key]["ax"]) + abs(particles[key]["ay"]) + abs(particles[key]["az"])
def dist(key): return abs(particles[key]["px"]) + abs(particles[key]["py"]) + abs(particles[key]["pz"])

#particle with lowest acceleration will be the closest to origin in long term
min = 1e30
closest_particles = []
for key in particles:
    if accel(key) < min: min = accel(key)

#if there are more particles with lowest acceleration
for key in particles:
    if accel(key) == min: closest_particles.append(key)

#accel same for closest particles ^= get lowest position for closest particle
min = 1e30
closest_particle = -1
for key in closest_particles:
    if dist(key) < min:
        closest_particle = key
        min = dist(key)

print(closest_particle)

#Millisecond 20: Second half
def equal(key1, key2): return particles[key1]["px"] == particles[key2]["px"] and particles[key1]["py"] == particles[key2]["py"] and particles[key1]["pz"] == particles[key2]["pz"]
def pos(key): return "{0}:{1}:{2}".format(particles[key]["px"], particles[key]["py"], particles[key]["pz"])
def inc(key):
    particles[key]["vx"] += particles[key]["ax"]
    particles[key]["vy"] += particles[key]["ay"]
    particles[key]["vz"] += particles[key]["az"]
    particles[key]["px"] += particles[key]["vx"]
    particles[key]["py"] += particles[key]["vy"]
    particles[key]["pz"] += particles[key]["vz"]


collisions = {}
#increase range if answer is not correct
#find collisions and remove them from particles
for i in range(100):
    for key in particles: inc(key)

    for key1 in particles:
        for key2 in particles:
            if key1 != key2 and equal(key1, key2):
                if key1 not in collisions: collisions.append(key1)
                if key2 not in collisions: collisions.append(key2)

    for key in collisions:
        particles.pop(key)

    collisions.clear()

print(len(particles))
