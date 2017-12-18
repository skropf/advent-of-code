#Millisecond 18
import os
import threading
import queue

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/18input.txt", 'r')

instructions = file.read().strip().split('\n')

def value(elem, registry):
    try: return int(elem)
    except:
        if elem not in registry: registry[elem] = 0
        return registry[elem]

#Millisecond 18: First half
def execute(instructions):
    registry = {}
    last_snd_played = 0
    i = 0

    while True:
        instruction = instructions[i]

        elems = instruction.split(' ')
        operation = elems[0]

        if operation == "snd":
            last_snd_played = value(elems[1], registry)
            i += 1
        if operation == "set":
            registry[elems[1]] = value(elems[2], registry)
            i += 1
        if operation == "add":
            registry[elems[1]] = value(elems[1], registry) + value(elems[2], registry)
            i += 1
        if operation == "mul":
            registry[elems[1]] = value(elems[1], registry) * value(elems[2], registry)
            i += 1
        if operation == "mod":
            registry[elems[1]] = value(elems[1], registry) % value(elems[2], registry)
            i += 1
        if operation == "rcv":
            return last_snd_played
            i += 1
        if operation == "jgz":
            x = value(elems[1], registry)
            if x > 0:
                i += value(elems[2], registry)
            else:
                i += 1

print(execute(instructions))

#Millisecond 18: Second half
def execute_parallel(id, instructions, snd_queue, rcv_queue):
    registry = {}
    registry['p'] = id
    i = 0
    sndcount = 0

    while True:
        instruction = instructions[i]

        elems = instruction.split(' ')
        operation = elems[0]

        if operation == "snd":
            snd_queue.put(value(elems[1], registry))

            if id == 1:
                sndcount += 1
                print(sndcount)
            i += 1
        if operation == "set":
            registry[elems[1]] = value(elems[2], registry)
            i += 1
        if operation == "add":
            registry[elems[1]] = value(elems[1], registry) + value(elems[2], registry)
            i += 1
        if operation == "mul":
            registry[elems[1]] = value(elems[1], registry) * value(elems[2], registry)
            i += 1
        if operation == "mod":
            registry[elems[1]] = value(elems[1], registry) % value(elems[2], registry)
            i += 1
        if operation == "rcv":
            registry[elems[1]] = rcv_queue.get()
            i += 1
        if operation == "jgz":
            x = value(elems[1], registry)
            if x > 0:
                i += value(elems[2], registry)
            else:
                i += 1



q1 = queue.Queue()
q2 = queue.Queue()

program0 = threading.Thread(target=execute_parallel, args=(0, instructions, q1, q2))
program1 = threading.Thread(target=execute_parallel, args=(1, instructions, q2, q1))

program0.start()
program1.start()
