#Millisecond 19
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/19input.txt", 'r')

lines = file.read().split('\n')


#set end_char and diagram_chars manually
diagram_chars = ['+', '-', '|', ' ']
end_char = 'Y'

#get longest line to make all equal length (otherwise out-of-bounds error)
max = 0
for line in lines:
    if max < len(line): max = len(line)

#set routing_diagram and letters for solution
letters = []
routing_diagram = []
for line in lines:
    while len(line) < max: line += (' ')
    routing_diagram.append(line)
    for char in line:
        if char not in diagram_chars: letters.append(char)

def running(routing_diagram, line, index, dir, steps):
    solution = ""
    cur_char = ""

    while cur_char != end_char:
        cur_char = routing_diagram[line][index]
        if cur_char in letters: solution += cur_char

        if dir == "up":
            next = routing_diagram[line-1][index]
            nextnext = routing_diagram[line-2][index] if line-2 >= 0 else None
            left_next = routing_diagram[line-1][index-1] if index-1 >= 0 else None
            right_next = routing_diagram[line-1][index+1] if index+1 < len(routing_diagram[line-1]) else None
            line -= 1

            if next == "|" or nextnext == "|" or next in letters or nextnext in letters: dir = "up"
            elif next == "+":
                if left_next == "-": dir = "left"
                if right_next == "-": dir = "right"

        elif dir == "down":
            next = routing_diagram[line+1][index]
            nextnext = routing_diagram[line+2][index] if line+2 < len(routing_diagram) else None
            left_next = routing_diagram[line+1][index-1] if index-1 >= 0 else None
            right_next = routing_diagram[line+1][index+1] if index+1 < len(routing_diagram[line+1]) else None
            line += 1

            if next == "|" or nextnext == "|" or next in letters or nextnext in letters: dir = "down"
            elif next == "+":
                if left_next == "-": dir = "left"
                if right_next == "-": dir = "right"

        elif dir == "left":
            next = routing_diagram[line][index-1]
            nextnext = routing_diagram[line][index-2] if index-2 >= 0 else None
            up_next = routing_diagram[line-1][index-1] if line-1 >= 0 else None
            down_next = routing_diagram[line+1][index-1] if line+1 < len(routing_diagram) else None
            index -= 1

            if next == "-" or nextnext == "-" or next in letters or nextnext in letters: dir = "left"
            elif next == "+":
                if up_next == "|": dir = "up"
                if down_next == "|": dir = "down"

        elif dir == "right":
            next = routing_diagram[line][index+1]
            nextnext = routing_diagram[line][index+2] if index+2 < len(routing_diagram[line]) else None
            up_next = routing_diagram[line-1][index+1] if line-1 >= 0 else None
            down_next = routing_diagram[line+1][index+1] if line+1 < len(routing_diagram) else None
            index += 1

            if next == "-" or nextnext == "-" or next in letters or nextnext in letters: dir = "right"
            elif next == "+":
                if up_next == "|": dir = "up"
                if down_next == "|": dir = "down"

        steps += 1

    return (solution, steps)

line = 0
index = routing_diagram[line].index('|')
result = running(routing_diagram, line, index, "down", 0)
print(result[0])
print(result[1])
