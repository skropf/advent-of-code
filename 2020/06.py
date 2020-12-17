
fh = open('06.input', 'r')
puzzle = [x.strip() for x in fh.readlines()]

qsum, qsum2 = 0, 0
questions = []
for line in puzzle:
    if line != "": questions.append(line)
    else:
        qsum += len(list(set(''.join(questions))))

        res = set("abcdefghijklmnopqrstuvwxyz")
        for line in questions:
            res = res & set(line)
        qsum2 += len(res)

        questions = []

print("Part 1:", str(qsum))
print("Part 2:", str(qsum2))

