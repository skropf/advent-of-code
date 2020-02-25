### DAY 3 - Part 1

# thoughts: create big array where one cable is represented as #, the other as + and intersections
# with * => find the closest * from the origin point

input = open('03.input', 'r')
wire1 = input.readline().split(',')
wire2 = input.readline().split(',')

# lets just trace the two wirepaths and examine both later for closest point to origin
# we use a number here for both positions, to be able to convert them to sets and use the intersection function
# (x => left of decimal point, y => right of decimal point)
# for the y values we start at .5 because otherwise we would get wrong results in negative y direction

wirepath1 = [0.5]
wirepath2 = [0.5]

for route1, route2 in zip(wire1, wire2):

    distance1 = int(route1[1:])
    for i in range(distance1):
        last_pos = wirepath1.pop()
        wirepath1.append(last_pos)

        if route1[0] == 'U':
            last_pos += 0.00000001
        elif route1[0] == 'D':
            last_pos -= 0.00000001
        elif route1[0] == 'L':
            last_pos -= 1
        elif route1[0] == 'R':
            last_pos += 1
        else:
            # should not be happening
            print('Unknown direction!')
        
        wirepath1.append(round(last_pos, 8))

    distance2 = int(route2[1:])
    for i in range(distance2):
        last_pos = wirepath2.pop()
        wirepath2.append(last_pos)

        if route2[0] == 'U':
            last_pos += 0.00000001
        elif route2[0] == 'D':
            last_pos -= 0.00000001
        elif route2[0] == 'L':
            last_pos -= 1
        elif route2[0] == 'R':
            last_pos += 1
        else:
            # should not be happening
            print('Unknown direction!')
        
        wirepath2.append(round(last_pos, 8))

# get all intersections
result = list(set(wirepath1).intersection(wirepath2))

distances = []
for intersection in result:
    x = int(intersection)
    # calculate y value correctly by bringing it to 0 or 1, then bringing all to 0.00..., finally making an integer
    y = abs(round(-0.5 - round(intersection - x, 8), 8))
    if y >= 1.0: y = y - 1
    y = int(round(y * 100000000))
    
    distances.append(abs(x) + y)

# remove the overlapping origin point
distances.remove(0)
# print shortest distance
print('Shortest distance to the intersection:', min(distances))

### DAY 3 - Part 2

# just get the indeces of the intersections in the wirepaths, append them to a new list and get the min value
wire_distances = []
for intersection in result:
    distance_wire1 = wirepath1.index(intersection)
    distance_wire2 = wirepath2.index(intersection)

    wire_distances.append(distance_wire1 + distance_wire2)

# removing origin point
wire_distances.remove(0)
# print shortest distance from each wire
print('Shortest distance from both wires to intersection:', min(wire_distances))