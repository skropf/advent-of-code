
fh = open('01.input', 'r')
puzzle = sorted([int(x.strip()) for x in fh.readlines()])
size = len(puzzle)

# Part 1
result_found = False
for start in range(size):
    if result_found: break
    for end in range(size - 1, 0, -1):
        if puzzle[start] + puzzle[end] > 2020: continue
        if puzzle[start] + puzzle[end] == 2020:
            print("Solution:", str(puzzle[start]), "+", str(puzzle[end]))
            print("Found result:", str(puzzle[start] * puzzle[end]))
            result_found = True
        if puzzle[start] + puzzle[end] < 2020: break

# Part 2
for i in range(size):
    for j in range(size):
        for k in range(size):
            if (puzzle[i] + puzzle[j] + puzzle[k]) == 2020:
                print("Solution:", str(puzzle[i]), "+", str(puzzle[j]), "+", str(puzzle[k]))
                print("Found result:", str(puzzle[i] * puzzle[j] * puzzle[k]))
                exit()