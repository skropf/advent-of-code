content = open('02.input', 'r').readlines()

scores1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}
scores2 = {
    'A X': 3,
    'B X': 1,
    'C X': 2,
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,
    'A Z': 8,
    'B Z': 9,
    'C Z': 7
}

score1 = 0
score2 = 0
for line in content:
    score1 += scores1[line.strip()]
    score2 += scores2[line.strip()]

print(score1)
print(score2)