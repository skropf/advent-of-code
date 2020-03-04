### Day 7 - Part 1

puzzle_orig = open('07.input', 'r')
puzzle = [int(x) for x in puzzle_orig.read().split(',')]

class Amplifier(object):
    def __init__(self, name, puzzle, setting):
        from copy import copy
        self.name = name
        self.puzzle = copy(puzzle)
        self.setting = setting
        self.first_run = True
        self.instruction_pointer = 0

    def run(self, signal):
        while self.instruction_pointer < len(self.puzzle):
            op_code = self.puzzle[self.instruction_pointer]
            #addition
            if op_code % 100 == 1:
                if op_code % 1000 > 100: parameter1 = self.puzzle[self.instruction_pointer+1]
                else: parameter1 = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: parameter2 = self.puzzle[self.instruction_pointer+2]
                else: parameter2 = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                self.puzzle[self.puzzle[self.instruction_pointer+3]] = parameter1 + parameter2
                self.instruction_pointer += 4
            # multiplication
            elif op_code % 100 == 2:
                if op_code % 1000 > 100: parameter1 = self.puzzle[self.instruction_pointer+1]
                else: parameter1 = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: parameter2 = self.puzzle[self.instruction_pointer+2]
                else: parameter2 = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                self.puzzle[self.puzzle[self.instruction_pointer+3]] = parameter1 * parameter2
                self.instruction_pointer += 4
            # take input and store
            elif op_code % 100 == 3:
                if self.first_run:
                    self.puzzle[self.puzzle[self.instruction_pointer+1]] = self.setting
                    self.first_run = False
                else:
                    self.puzzle[self.puzzle[self.instruction_pointer+1]] = signal
                self.instruction_pointer += 2
            # outputs value at address
            elif op_code % 100 == 4:
                if op_code % 1000 > 100: parameter = self.puzzle[self.instruction_pointer+1]
                else: parameter = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                
                self.instruction_pointer += 2
                return parameter
            # jump if first parameter is not zero
            elif op_code % 100 == 5:
                if op_code % 1000 > 100: parameter = self.puzzle[self.instruction_pointer+1]
                else: parameter = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: jumping_to = self.puzzle[self.instruction_pointer+2]
                else: jumping_to = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                if parameter != 0: self.instruction_pointer = jumping_to
                else: self.instruction_pointer += 3
            # jump if first parameter is zero
            elif op_code % 100 == 6:
                if op_code % 1000 > 100: parameter = self.puzzle[self.instruction_pointer+1]
                else: parameter = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: jumping_to = self.puzzle[self.instruction_pointer+2]
                else: jumping_to = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                if parameter == 0: self.instruction_pointer = jumping_to
                else: self.instruction_pointer += 3
            # store 1 if less than
            elif op_code % 100 == 7:
                if op_code % 1000 > 100: parameter1 = self.puzzle[self.instruction_pointer+1]
                else: parameter1 = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: parameter2 = self.puzzle[self.instruction_pointer+2]
                else: parameter2 = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                if parameter1 < parameter2: self.puzzle[self.puzzle[self.instruction_pointer+3]] = 1
                else: self.puzzle[self.puzzle[self.instruction_pointer+3]] = 0
                self.instruction_pointer += 4
            # store 1 if equal
            elif op_code % 100 == 8:
                if op_code % 1000 > 100: parameter1 = self.puzzle[self.instruction_pointer+1]
                else: parameter1 = self.puzzle[self.puzzle[self.instruction_pointer+1]]
                if op_code % 10000 > 1000: parameter2 = self.puzzle[self.instruction_pointer+2]
                else: parameter2 = self.puzzle[self.puzzle[self.instruction_pointer+2]]
                if parameter1 == parameter2: self.puzzle[self.puzzle[self.instruction_pointer+3]] = 1
                else: self.puzzle[self.puzzle[self.instruction_pointer+3]] = 0
                self.instruction_pointer += 4
            # break
            elif op_code % 100 == 99:
                #print("Halted.")
                return
            else:
                ### if printed, something is wrong
                print('Unknown operation', op_code % 100,'in AMP', self.name + '.', 'Halted.')
                return

from itertools import permutations
thruster_permutations = list(permutations([0, 1, 2, 3, 4, 5], 5))

max_thrust = 0
setting = []
for tp in thruster_permutations:
    amp_a = Amplifier('A', puzzle, tp[0])
    amp_b = Amplifier('B', puzzle, tp[1])
    amp_c = Amplifier('C', puzzle, tp[2])
    amp_d = Amplifier('D', puzzle, tp[3])
    amp_e = Amplifier('E', puzzle, tp[4])

    thrust = amp_e.run(amp_d.run(amp_c.run(amp_b.run(amp_a.run(0)))))

    if max_thrust < thrust:
        max_thrust = thrust
        setting = tp

print("Maximum thrust:", max_thrust, "with amplifier setting:", setting)

### Day 7 - Part 2

puzzle_orig.seek(0)
puzzle = [int(x) for x in puzzle_orig.read().split(',')]

phase_settings = list(permutations([5,6,7,8,9], 5))

amps = {}
max_thrust, setting = 0, []
for phase in phase_settings:
    amps['a'] = Amplifier('A', puzzle, phase[0])
    amps['b'] = Amplifier('B', puzzle, phase[1])
    amps['c'] = Amplifier('C', puzzle, phase[2])
    amps['d'] = Amplifier('D', puzzle, phase[3])
    amps['e'] = Amplifier('E', puzzle, phase[4])

    def calc(amps, signal, prev_signal):
        if signal == None: return prev_signal
        return calc(amps, amps['e'].run(amps['d'].run(amps['c'].run(amps['b'].run(amps['a'].run(signal))))), signal)
    
    thrust = calc(amps, 0, 0)
    
    if thrust and max_thrust < thrust:
        max_thrust = thrust
        setting = phase

print("Max Thrust with loopback:", max_thrust, "with setting:", setting)