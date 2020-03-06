### Day 11 - Part 1

puzzle_orig = open('11.input', 'r')
program = [int(x) for x in puzzle_orig.read().split(',')]

class IntcodeComputer(object):
    def __init__(self, name, memory):
        from copy import copy
        self.name = name
        self.memory = copy(memory)
        self.memory += [0] * len(memory) * 100
        self.instruction_pointer = 0
        self.relative_base = 0

    def run(self, signal):
        while True:
            op_code = self.memory[self.instruction_pointer]
            #addition
            if op_code % 100 == 1:
                if op_code % 1000 > 200: parameter1 = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter1 = self.memory[self.instruction_pointer+1]
                else: parameter1 = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: parameter2 = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: parameter2 = self.memory[self.instruction_pointer+2]
                else: parameter2 = self.memory[self.memory[self.instruction_pointer+2]]
                
                if op_code % 100000 > 20000: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = parameter1 + parameter2
                elif op_code % 100000 > 10000: self.memory[self.instruction_pointer+3] = parameter1 + parameter2
                else: self.memory[self.memory[self.instruction_pointer+3]] = parameter1 + parameter2
                self.instruction_pointer += 4
            # multiplication
            elif op_code % 100 == 2:
                if op_code % 1000 > 200: parameter1 = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter1 = self.memory[self.instruction_pointer+1]
                else: parameter1 = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: parameter2 = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: parameter2 = self.memory[self.instruction_pointer+2]
                else: parameter2 = self.memory[self.memory[self.instruction_pointer+2]]
                
                if op_code % 100000 > 20000: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = parameter1 * parameter2
                elif op_code % 100000 > 10000: self.memory[self.instruction_pointer+3] = parameter1 * parameter2
                else: self.memory[self.memory[self.instruction_pointer+3]] = parameter1 * parameter2
                self.instruction_pointer += 4
            # take input and store
            elif op_code % 100 == 3:
                if op_code % 1000 > 200: self.memory[self.relative_base+self.memory[self.instruction_pointer+1]] = signal
                elif op_code % 1000 > 100: self.memory[self.instruction_pointer+1] = signal
                else: self.memory[self.memory[self.instruction_pointer+1]] = signal
                
                self.instruction_pointer += 2
            # outputs value at address
            elif op_code % 100 == 4:
                if op_code % 1000 > 200: parameter = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter = self.memory[self.instruction_pointer+1]
                else: parameter = self.memory[self.memory[self.instruction_pointer+1]]
                
                self.instruction_pointer += 2
                return parameter
            # jump if first parameter is not zero
            elif op_code % 100 == 5:
                if op_code % 1000 > 200: parameter = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter = self.memory[self.instruction_pointer+1]
                else: parameter = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: jumping_to = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: jumping_to = self.memory[self.instruction_pointer+2]
                else: jumping_to = self.memory[self.memory[self.instruction_pointer+2]]
                
                if parameter != 0: self.instruction_pointer = jumping_to
                else: self.instruction_pointer += 3
            # jump if first parameter is zero
            elif op_code % 100 == 6:
                if op_code % 1000 > 200: parameter = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter = self.memory[self.instruction_pointer+1]
                else: parameter = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: jumping_to = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: jumping_to = self.memory[self.instruction_pointer+2]
                else: jumping_to = self.memory[self.memory[self.instruction_pointer+2]]
                
                if parameter == 0: self.instruction_pointer = jumping_to
                else: self.instruction_pointer += 3
            # store 1 if less than
            elif op_code % 100 == 7:
                if op_code % 1000 > 200: parameter1 = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter1 = self.memory[self.instruction_pointer+1]
                else: parameter1 = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: parameter2 = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: parameter2 = self.memory[self.instruction_pointer+2]
                else: parameter2 = self.memory[self.memory[self.instruction_pointer+2]]
                
                if op_code % 100000 > 20000:
                    if parameter1 < parameter2: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = 1
                    else: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = 0
                if op_code % 100000 > 10000:
                    if parameter1 < parameter2: self.memory[self.instruction_pointer+3] = 1
                    else: self.memory[self.instruction_pointer+3] = 0
                else:
                    if parameter1 < parameter2: self.memory[self.memory[self.instruction_pointer+3]] = 1
                    else: self.memory[self.memory[self.instruction_pointer+3]] = 0
                
                self.instruction_pointer += 4
            # store 1 if equal
            elif op_code % 100 == 8:
                if op_code % 1000 > 200: parameter1 = self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: parameter1 = self.memory[self.instruction_pointer+1]
                else: parameter1 = self.memory[self.memory[self.instruction_pointer+1]]
                
                if op_code % 10000 > 2000: parameter2 = self.memory[self.relative_base+self.memory[self.instruction_pointer+2]]
                elif op_code % 10000 > 1000: parameter2 = self.memory[self.instruction_pointer+2]
                else: parameter2 = self.memory[self.memory[self.instruction_pointer+2]]
                
                if op_code % 100000 > 20000:
                    if parameter1 == parameter2: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = 1
                    else: self.memory[self.relative_base+self.memory[self.instruction_pointer+3]] = 0
                if op_code % 100000 > 10000:
                    if parameter1 == parameter2: self.memory[self.instruction_pointer+3] = 1
                    else: self.memory[self.instruction_pointer+3] = 0
                else:
                    if parameter1 == parameter2: self.memory[self.memory[self.instruction_pointer+3]] = 1
                    else: self.memory[self.memory[self.instruction_pointer+3]] = 0
                
                self.instruction_pointer += 4
            # set relative base
            elif op_code % 100 == 9:
                if op_code % 1000 > 200: self.relative_base += self.memory[self.relative_base+self.memory[self.instruction_pointer+1]]
                elif op_code % 1000 > 100: self.relative_base += self.memory[self.instruction_pointer+1]
                else: self.relative_base += self.memory[self.memory[self.instruction_pointer+1]]
                
                self.instruction_pointer += 2
            # break
            elif op_code % 100 == 99:
                return
            else:
                ### if printed, something is wrong
                print('Unknown operation', op_code % 100, 'in', self.name + '.', 'Halted.')
                return

computer = IntcodeComputer("EHPR", program)

def paint(signal):
    position = [0, 0]
    view_direction = [0, -1] # look upwards
    tiles_painted = {}
    color, direction = 0, 0

    while True:
        color = computer.run(signal)
        direction = computer.run(signal)

        if color == None or direction == None: break

        tiles_painted[tuple(position)] = color
        if direction == 1:
            if view_direction == [0, -1]: view_direction = [1, 0] # up -> right
            elif view_direction == [1, 0]: view_direction = [0, 1] # right -> down
            elif view_direction == [0, 1]: view_direction = [-1, 0] # down -> left
            elif view_direction == [-1, 0]: view_direction = [0, -1] # left -> up
        else:
            if view_direction == [0, -1]: view_direction = [-1, 0] # up -> left
            elif view_direction == [1, 0]: view_direction = [0, -1] # right -> up
            elif view_direction == [0, 1]: view_direction = [1, 0] # down -> right
            elif view_direction == [-1, 0]: view_direction = [0, 1] # left -> down
        
        position = [x + y for x, y in zip(position, view_direction)]

        if tuple(position) in tiles_painted.keys(): signal = tiles_painted[tuple(position)]
        else: signal = 0

    return tiles_painted

tiles = paint(0)
print("Number of at least once painted panels:", len(tiles))

### Day 11 - Part 2

computer = IntcodeComputer("EHPR", program)
tiles = paint(1)

minmax = [0, 0]
for key in tiles.keys():
    if key[0] > minmax[1]: minmax[1] = key[0]
    if key[1] > minmax[1]: minmax[1] = key[1]
    if key[0] < minmax[0]: minmax[0] = key[0]
    if key[1] < minmax[0]: minmax[0] = key[1]

length = abs(minmax[0]) + abs(minmax[1]) + 1

panels = [[0 for y in range(length)] for x in range(length)]

for item in tiles.items():
    panels[item[0][1]][item[0][0]] = item[1]

for line in panels:
    if 1 in line: print(line)
    