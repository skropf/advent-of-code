

fh = open('03.input', 'r')
puzzle = [x.strip() for x in fh.readlines()]

end = len(puzzle)
size = len(puzzle[0])

def count_trees(slope):
    trees = 0
    position = [0, 0]
    while position[1] < end:
        if position[0] >= size: position[0] -= size

        if puzzle[position[1]][position[0]] == '#': trees += 1

        position[0] += slope[0]
        position[1] += slope[1]
    
    return trees

print("Part 1:", str(count_trees((3, 1))))
print("Part 2:", str(count_trees((1, 1)) * count_trees((3, 1)) * count_trees((5, 1)) * count_trees((7, 1)) * count_trees((1, 2))))