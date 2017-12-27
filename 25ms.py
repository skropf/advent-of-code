#Millisecond 25
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/25input.txt", 'r')

cur_state = file.readline()[-3]
steps_checksum = int(file.readline().split(' ')[-2])

#putting input into data structure
i = 0
states = {}
content = file.read().split('\n')
while i < len(content):
    if content[i].startswith("In state"):
        states[content[i][-2]] = {'0':[int(content[i+2][-2]), content[i+3].split(' ')[-1].replace('.', ''), content[i+4][-2]], '1':[int(content[i+6][-2]), content[i+7].split(' ')[-1].replace('.', ''), content[i+8][-2]]}
        i += 8
    i += 1

#going through the states accordingly until steps to calculate checksum is reached
cur_index = 0
tape = [0]
for i in range(steps_checksum):
    if tape[cur_index] == 0:
        tape[cur_index] = states[cur_state]['0'][0]

        if states[cur_state]['0'][1] == "right":
            if len(tape) == cur_index + 1: tape.append(0)
            cur_index += 1
        else:
            if cur_index == 0: tape.insert(0, 0)
            else: cur_index -= 1

        cur_state = states[cur_state]['0'][2]
    else:
        tape[cur_index] = states[cur_state]['1'][0]

        if states[cur_state]['1'][1] == "right":
            if len(tape) == cur_index + 1: tape.append(0)
            cur_index += 1
        else:
            if cur_index == 0: tape.insert(0, 0)
            else: cur_index -= 1

        cur_state = states[cur_state]['1'][2]

print(sum(tape))
