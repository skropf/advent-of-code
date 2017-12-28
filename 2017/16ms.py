#Millisecond 16
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/16input.txt", 'r')

moves = file.read().strip().split(',')
dancing_programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

#Millisecond 16: First half
def dance(programs):
    for move in moves:
        #Spin
        if move.startswith('s'):
            to_move = int(move[1:])

            programs = programs[-to_move:] + programs[:len(programs)-to_move]

        #Exchange
        if move.startswith('x'):
            pos1 = int(move[1:].split('/')[0])
            pos2 = int(move[1:].split('/')[1])

            bufprog = programs[pos1]

            programs[pos1] = programs[pos2]
            programs[pos2] = bufprog

        #Partner
        if move.startswith('p'):
            pos1 = programs.index(move[1:].split('/')[0])
            pos2 = programs.index(move[1:].split('/')[1])

            bufprog = programs[pos1]

            programs[pos1] = programs[pos2]
            programs[pos2] = bufprog

    return programs

#programs after dancing once
print("".join(dance(dancing_programs)))

#Millisecond 16: Second half
programs = dancing_programs
buffer_programs = []
steps_for_repetition = 0

#Look how many dancing rounds it takes until pattern repeats
while programs not in buffer_programs:
    buffer_programs.append(programs)
    programs = dance(programs)

    steps_for_repetition += 1

#dancing takes to long for 1B times - take shortcut
steps_to_solution = 1000000000 % steps_for_repetition

#getting output after running "1B times", because of repetition pattern of dancing programs
programs = dancing_programs
for i in range(steps_to_solution):
    programs = dance(programs)

print("".join(programs))
