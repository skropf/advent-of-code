#Millisecond 13
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/13input.txt", 'r')

firewall = {}
for line in file:
    elems = line.strip().split(": ")

    depth = int(elems[0])
    r = int(elems[1])
    steps = (r - 1) * 2

    firewall[depth] = [r, steps]

top_layer = max(firewall.keys())

#Millisecond 13: First half
def calc_severity(picosecond_start=0):
    severity = 0
    picosecond = picosecond_start
    caught = False
    for i in range(top_layer + 1):
        if i not in firewall.keys():
            picosecond += 1
            continue

        position = picosecond % firewall[i][1]

        if position == 0:
            caught = True
            severity += firewall[i][0] * i

        picosecond += 1

    return (severity, caught)

print(calc_severity()[0])

#Millisecond 13: Second half
picosecond_start = 0
while True:
    if not calc_severity(picosecond_start)[1]: break
    picosecond_start += 1

print(picosecond_start)
