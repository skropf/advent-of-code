import queue

def print_top_crates(stacks):
    nr_of_stacks = len(stacks.keys())
    print(''.join([stacks[i+1].get() for i in range(nr_of_stacks)]))

def print_stacks(stacks):
    nr_of_stacks = len(stacks.keys())
    for i in range(nr_of_stacks):
        print(stacks[i+1].queue)

def init_stacks(content):
    stacks = {}
    nr_of_stacks = [int(line.strip().split(' ')[-1]) for line in content if line.startswith(' ')][0]

    for i in range(nr_of_stacks):
        stacks[i+1] = queue.LifoQueue()
        for line in reversed(content):
            if line.startswith(('move', ' ', '\n')): continue
            crate = line[1+(i*4)]
            if crate != ' ': stacks[i+1].put(crate)
    
    return stacks

def part_one(content, stacks):
    for line in content:
        if line.startswith('move'):
            nr_of_crates, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])

            for i in range(nr_of_crates):
                crate = stacks[from_stack].get()
                stacks[to_stack].put(crate)

    print_top_crates(stacks)

def part_two(content, stacks):
    for line in content:
        if line.startswith('move'):
            nr_of_crates, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]), int(line.split(' ')[5])

            
            crates = [stacks[from_stack].get() for i in range(nr_of_crates)]
            for crate in reversed(crates):
                stacks[to_stack].put(crate)
    
    print_top_crates(stacks)

content = open('05.input', 'r').readlines()
stacks = init_stacks(content)
part_one(content, stacks)
stacks = init_stacks(content)
part_two(content, stacks)