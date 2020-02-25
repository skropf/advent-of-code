### Day 5 - Part 1

puzzle = open('05.input', 'r')
puzzle = [int(x) for x in puzzle.read().split(',')]

instructions = []
index = 0
while index < len(puzzle):
    op_code = puzzle[index]
    #addition
    if op_code % 100 == 1:
        if op_code % 1000 > 100: parameter1 = puzzle[index+1]
        else: parameter1 = puzzle[puzzle[index+1]]
        if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
        else: parameter2 = puzzle[puzzle[index+2]]

        instructions.append(puzzle[index:index+4])

        puzzle[puzzle[index+3]] = parameter1 + parameter2
        index += 4
    # multiplication
    elif op_code % 100 == 2:
        if op_code % 1000 > 100: parameter1 = puzzle[index+1]
        else: parameter1 = puzzle[puzzle[index+1]]
        if op_code % 10000 > 1000: parameter2 = puzzle[index+2]
        else: parameter2 = puzzle[puzzle[index+2]]

        instructions.append(puzzle[index:index+4])

        puzzle[puzzle[index+3]] = parameter1 + parameter2
        index += 4
    # take input and store
    elif op_code % 100 == 3:
        instructions.append(puzzle[index:index+2])

        puzzle[puzzle[index+1]] = int(input())
        index += 2
    # outputs value at address
    elif op_code % 100 == 4:
        if op_code % 1000 > 100: parameter = puzzle[index+1]
        else: parameter = puzzle[puzzle[index+1]]
        print(instructions)
        print(puzzle)
        print(parameter)
        instructions.append(puzzle[index:index+2])
        index += 2
    # break
    elif op_code % 100 == 99:
        instructions.append(puzzle[index])
        #print('Value at position 0 is:', puzzle[0])
        break
    else:
        ### if printed, something is wrong
        print('unknown operation')
        index += 1