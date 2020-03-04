### Day 7 - Part 1

puzzle_orig = open('07.input', 'r')
puzzle = [int(x) for x in puzzle_orig.read().split(',')]

class Amplifier(object):
    def __init__(self, name, puzzle, setting):
        self.name = name
        self.puzzle = puzzle
        self.setting = setting
        self.first_run = True

    def run(self, signal):
        index = 0
        while index < len(puzzle):
            op_code = puzzle[index]
            #addition
            if op_code % 100 == 1:
                if op_code % 1000 > 100: parameter1 = puzzle[index+1]
                else: parameter1 = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
                else: parameter2 = puzzle[puzzle[index+2]]
                puzzle[puzzle[index+3]] = parameter1 + parameter2
                index += 4
            # multiplication
            elif op_code % 100 == 2:
                if op_code % 1000 > 100: parameter1 = puzzle[index+1]
                else: parameter1 = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
                else: parameter2 = puzzle[puzzle[index+2]]
                puzzle[puzzle[index+3]] = parameter1 * parameter2
                index += 4
            # take input and store
            elif op_code % 100 == 3:
                if self.first_run:
                    puzzle[puzzle[index+1]] = self.setting
                    self.first_run = False
                else:
                    puzzle[puzzle[index+1]] = signal
                index += 2
            # outputs value at address
            elif op_code % 100 == 4:
                if op_code % 1000 > 100: parameter = puzzle[index+1]
                else: parameter = puzzle[puzzle[index+1]]
                
                index += 2
                return parameter
            # jump if first parameter is not zero
            elif op_code % 100 == 5:
                if op_code % 1000 > 100: parameter = puzzle[index+1]
                else: parameter = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: jumping_to = puzzle[index+2]
                else: jumping_to = puzzle[puzzle[index+2]]
                if parameter != 0: index = jumping_to
                else: index += 3
            # jump if first parameter is zero
            elif op_code % 100 == 6:
                if op_code % 1000 > 100: parameter = puzzle[index+1]
                else: parameter = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: jumping_to = puzzle[index+2]
                else: jumping_to = puzzle[puzzle[index+2]]
                if parameter == 0: index = jumping_to
                else: index += 3
            # store 1 if less than
            elif op_code % 100 == 7:
                if op_code % 1000 > 100: parameter1 = puzzle[index+1]
                else: parameter1 = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
                else: parameter2 = puzzle[puzzle[index+2]]
                if parameter1 < parameter2: puzzle[puzzle[index+3]] = 1
                else: puzzle[puzzle[index+3]] = 0
                index += 4
            # store 1 if equal
            elif op_code % 100 == 8:
                if op_code % 1000 > 100: parameter1 = puzzle[index+1]
                else: parameter1 = puzzle[puzzle[index+1]]
                if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
                else: parameter2 = puzzle[puzzle[index+2]]
                if parameter1 == parameter2: puzzle[puzzle[index+3]] = 1
                else: puzzle[puzzle[index+3]] = 0
                index += 4
            # break
            elif op_code % 100 == 99:
                print("Halted.")
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

#puzzle = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
puzzle = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

phase_settings = list(permutations([9,8,7,6,5], 5))

amps = {}
max_thrust, setting = 0, []
for phase in phase_settings:
    amps['a'] = Amplifier('A', puzzle, phase[0])
    amps['b'] = Amplifier('B', puzzle, phase[1])
    amps['c'] = Amplifier('C', puzzle, phase[2])
    amps['d'] = Amplifier('D', puzzle, phase[3])
    amps['e'] = Amplifier('E', puzzle, phase[4])

    def calc(amps, signal):
        print(signal)
        if signal >= 139629729: return signal
        
        if signal == None: return

        signal = amps['e'].run(amps['d'].run(amps['c'].run(amps['b'].run(amps['a'].run(signal)))))

        return calc(amps, signal)
    
    try:
        thrust = calc(amps, 0)
    except Exception as e:
        print("error:", e)
    
    if thrust and max_thrust < thrust:
        max_thrust = thrust
        setting = tp
    exit()

print("Max Thrust with loopback:", max_thrust, "with setting:", setting)