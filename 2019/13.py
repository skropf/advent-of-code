### Day 13 - Part 1

puzzle_orig = open('13.input', 'r')
program = [int(x) for x in puzzle_orig.read().split(',')]

class IntcodeComputer(object):
    def __init__(self, name, memory):
        from copy import copy
        self.name = name
        self.memory = copy(memory)
        self.memory += [0] * len(memory) * 100
        self.instruction_pointer = 0
        self.relative_base = 0

    def run(self):
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
                if op_code % 1000 > 200: self.memory[self.relative_base+self.memory[self.instruction_pointer+1]] = int(input())
                elif op_code % 1000 > 100: self.memory[self.instruction_pointer+1] = int(input())
                else: self.memory[self.memory[self.instruction_pointer+1]] = int(input())
                
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

computer = IntcodeComputer("Arcade", program)

ids = { 0: 'empty', 1: 'wall', 2: 'block', 3: 'horizontal paddle', 4: 'ball'}
tiles = {}

while True:
    x_pos = computer.run()
    y_pos = computer.run()
    tile_id = computer.run()

    if tile_id == None: break

    tiles[(x_pos, y_pos)] = ids[tile_id]

print("Number of block tiles:", len([tile for tile in tiles.values() if tile == 'block']))

### Day 13 - Part 2

program[0] = 2
computer = IntcodeComputer("Arcade", program)

def draw_screen(tiles):
    size = max([tile[0] for tile in tiles.keys()] + [tile[1] for tile in tiles.keys()]) + 1
    screen = [[' ' for x in range(size)] for y in range(size)]

    for tile in tiles.items():
        screen[tile[0][0]][tile[0][1]] = tile[1]

    for line in screen:
        print(''.join(line))

ids = { 0: ' ', 1: 'W', 2: 'B', 3: '|', 4: 'O'}
tiles = {}
current_score = 0
while True:
    x_pos = computer.run()
    y_pos = computer.run()
    tile_id = computer.run()

    if tile_id == None: break
    if x_pos == -1 and y_pos == 0:
        current_score = tile_id
    else:
        tiles[(x_pos, y_pos)] = ids[tile_id]
        
    print("HIGHSCORE:",current_score)
    

    draw_screen(tiles)
    