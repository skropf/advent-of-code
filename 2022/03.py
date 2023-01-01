import itertools

content = open('03.input', 'r').readlines()

priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}

sum_priorities = 0
for line in content:
    length = len(line.strip())

    a = line[0:int(length/2)]
    b = line[int(length/2):length]

    diff = list(set(a).intersection(b))
    sum_priorities += priorities[diff[0]]

print(sum_priorities)


sum_priorities = 0
with open('03.input', 'r') as f:
    for l1,l2,l3 in itertools.zip_longest(*[f]*3):
        l1,l2,l3 = l1.strip(),l2.strip(),l3.strip()

        diff = list(set(l1).intersection(l2).intersection(l3))
        sum_priorities += priorities[diff[0]]

print(sum_priorities)