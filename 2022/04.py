content = open('04.input', 'r').readlines()

count_full, count_part = 0, 0
for line in content:
    p1, p2 = line.strip().split(',')
    p1, p2 = [int(x) for x in p1.split('-')], [int(x) for x in p2.split('-')]
    
    if (p1[0] >= p2[0] and p1[1] <= p2[1]) or \
       (p1[0] <= p2[0] and p1[1] >= p2[1]):
        count_full += 1
    
    if (p1[0] >= p2[0] and p1[1] <= p2[1]) or \
       (p1[0] <= p2[0] and p1[1] >= p2[1]) or \
       (p1[1] >= p2[0] and p1[1] <= p2[1]) or \
       (p1[0] <= p2[1] and p1[1] >= p2[1]):
        count_part += 1

print(count_full)
print(count_part)