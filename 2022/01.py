content = open('01.input', 'r').readlines()

weights = []
current_weight = 0
for line in content:
    if line != "\n":
        current_weight += int(line)
    else:
        weights.append(current_weight)
        current_weight = 0

print(max(weights))
print(sum(sorted(weights)[-3:]))