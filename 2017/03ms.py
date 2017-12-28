import math
import numpy as np

#Millisecond 3
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/03input.txt", 'r')

input = int(file.read())

#Millisecond 3: First half
root = 0
while root * root < input: root += 1

steps_back = root * root - input
while steps_back > math.floor(root / 2):
    steps_back -= math.floor(root / 2)

steps_from_center = math.floor(root / 2) - steps_back

print(steps_from_center + math.floor(root / 2))


#Millisecond 3: Second half
#helicalIndices from stackoverflow (insert link)
def helicalIndices(n):
    num = 0
    curr_x, dir_x, lim_x, curr_num_lim_x = 0, 1, 1, 2
    curr_y, dir_y, lim_y, curr_num_lim_y = -1, 1, 1, 3
    curr_rep_at_lim_x, up_x = 0, 1
    curr_rep_at_lim_y, up_y = 0, 1

    while num < n:
        if curr_x != lim_x:
            curr_x += dir_x
        else:
            curr_rep_at_lim_x += 1
            if curr_rep_at_lim_x == curr_num_lim_x - 1:
                if lim_x < 0:
                    lim_x = (-lim_x) + 1
                else:
                    lim_x = -lim_x
                curr_rep_at_lim_x = 0
                curr_num_lim_x += 1
                dir_x = -dir_x
        if curr_y != lim_y:
            curr_y = curr_y + dir_y
        else:
            curr_rep_at_lim_y += 1
            if curr_rep_at_lim_y == curr_num_lim_y - 1:
                if lim_y < 0:
                    lim_y = (-lim_y) + 1
                else:
                    lim_y = -lim_y
                curr_rep_at_lim_y = 0
                curr_num_lim_y += 1
                dir_y = -dir_y

        yield (curr_x, curr_y)
        num += 1

n = 31
middle = int(math.floor(n / 2))
a = np.zeros(shape=(n,n))

a[middle][middle] = 1
hi = helicalIndices(11*n)

for i in hi:
    i = (i[0] + middle, i[1] + middle)
    a[i[0]][i[1]] = a[i[0] + 1][i[1]] + a[i[0] + 1][i[1] + 1] + a[i[0]][i[1] + 1] + a[i[0] - 1][i[1] + 1] + a[i[0] - 1][i[1]] + a[i[0] - 1][i[1] - 1] + a[i[0]][i[1] - 1] + a[i[0] + 1][i[1] - 1]

    if a[i[0]][i[1]] > input:
        print(str(a[i[0]][i[1]]))
        break
