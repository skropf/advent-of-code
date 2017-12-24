#Millisecond 24
import os
from collections import Counter, deque

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/24input.txt", 'r')

connections = file.read().strip().split('\n')

#Millisecond 24: First + Second half
def create_bridges(links, type):
    #queue with all possible bridges and their status quo.
    #if bridge is finished (^= no next links) it will vanish from the queue
    queue = deque([(0, 0, 0, links)])

    while queue:
        #get/pop status quo of bridge, look if a link can be found (append new bridge to queue)
        #and run till queue is empty ^= no further next_links, yield results
        next_link, strength, length, links = queue.popleft()

        link_found = False
        for (link1, link2), occurence in links.items():
            if occurence == 0: continue

            if link1 == next_link:
                link_found = True
                new_links = Counter(links)
                new_links[link1, link2] -= 1
                new_links[link2, link1] -= 1
                queue.append((link2, strength + link1 + link2, length + 1, new_links))

        if not link_found:
            if type == "str": yield strength
            if type == "len": yield length, strength


links = Counter()
for conn in connections:
    link1, link2 = map(int, conn.split('/'))
    links[link1, link2] += 1
    links[link2, link1] += 1

print(max(create_bridges(links, "str")))
print(max(create_bridges(links, "len"))[1])
