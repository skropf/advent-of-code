### DAY 4 - Part 1

puzzle = open('04.input', 'r')
start, end = [int(x) for x in puzzle.read().split('-')]

def number_has_pair(number):
    number = list(str(number))
    return number[0] == number[1] or number[1] == number[2] or number[2] == number[3] or number[3] == number[4] or number[4] == number[5]

def number_not_decreasing(number):
    number = list(str(number))
    return number[0] <= number[1] and number[1] <= number[2] and number[2] <= number[3] and number[3] <= number[4] and number[4] <= number[5] 

count_valid = 0
for number in range(start, end):
    if number_not_decreasing(number) and number_has_pair(number):
        count_valid += 1

print('There are %d valid passwords' % count_valid)

### DAY 4 - Part 2

def number_has_pair_extended(number):
    number = list(str(number))
    return (number[0] == number[1] and number[1] != number[2]) or (number[0] != number[1] and number[1] == number[2] and number[2] != number[3]) or (number[1] != number[2] and number[2] == number[3] and number[3] != number[4]) or (number[2] != number[3] and number[3] == number[4] and number[4] != number[5]) or (number[3] != number[4] and number[4] == number[5])


count_valid = 0
for number in range(start, end):
    
    if number_not_decreasing(number) and number_has_pair_extended(number):
        count_valid += 1

print('There are %d valid passwords' % count_valid)