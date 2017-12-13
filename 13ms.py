#Millisecond 13
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/13input.txt", 'r')

firewall = {}
for line in file:
    elems = line.strip().split(": ")

    #define depth, range & steps/picoseconds needed for a whole iteration
    depth = int(elems[0])
    r = int(elems[1])
    steps = (r - 1) * 2

    #adding configuration to firewall
    firewall[depth] = [r, steps]

#setting max layer
top_layer = max(firewall.keys())

#Millisecond 13: First half
def calc_severity(picosecond_start=0):
    severity = 0
    picosecond = picosecond_start
    caught = False

    for i in range(top_layer + 1):
        #empty layer -> increase picosecond -> start anew
        if i not in firewall.keys():
            picosecond += 1
            continue

        #getting current position
        position = picosecond % firewall[i][1]

        #check if caught & set severity
        if position == 0:
            caught = True
            severity += firewall[i][0] * i

        picosecond += 1

    return (severity, caught)

print(calc_severity()[0])

#Millisecond 13: Second half
picosecond_start = 0
#bruteforce till not getting caught anymore (may take a while)
while True:
    if not calc_severity(picosecond_start)[1]: break
    picosecond_start += 1

print(picosecond_start)
