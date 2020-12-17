

fh = open('02.input', 'r')
puzzle = fh.readlines()

valid_passwords = 0
valid_passwords2 = 0
for line in puzzle:
    policy = [int(x) for x in line.split(' ')[0].split('-')]
    letter = line.split(':')[0].split(' ')[1]
    password = line.split(' ')[2]

    occurrences = password.count(letter)

    if occurrences >= policy[0] and occurrences <= policy[1]: valid_passwords += 1
    if (password[policy[0] - 1] == letter) ^ (password[policy[1] - 1] == letter):
        valid_passwords2 += 1

print("Valid passwords:", str(valid_passwords))

print("Valid passwords 2:", str(valid_passwords2))

