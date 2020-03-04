### Day 6 - Part 1

puzzle = open('06.input', 'r')
puzzle = [x.strip() for x in puzzle.readlines()]

## classes for data structure
class Node(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

class Tree(object):
    root = None

    def __init__(self):
        self.root = Node("COM", None)
    
    def find_node_by_name(self, node, name):
        if node.name == name: return node

        for n in node.children:
            ret = self.find_node_by_name(n, name)
            if ret is not None: return ret
    
    def gen_number_of_paths(self, node, count_of_paths):
        yield count_of_paths

        for n in node.children:
            yield from self.gen_number_of_paths(n, count_of_paths+1)
## end classes

def fill_tree(tree, orbits):
    index = 0
    while len(orbits) > 0:
        if index == len(orbits): index = 0

        o1, o2 = orbits[index].split(')')
        
        node = tree.find_node_by_name(tree.root, o1)

        if not node: index += 1
        else:
            # orbit found appending to node
            node.children.append(Node(o2, node))
            orbits.remove(orbits[index])

tree = Tree()
print("Saving orbits in tree data structure. This may take a while...")
fill_tree(tree, puzzle)

print("Number of Orbits:", sum(tree.gen_number_of_paths(tree.root, 0)))

### Day 6 - Part 2

you = tree.find_node_by_name(tree.root, "YOU")
san = tree.find_node_by_name(tree.root, "SAN")

switches_you, switches_san = [], []

# get all the nodes from YOU & SAN till root and then get the diff union
node = you
while node.parent:
    switches_you.append(node.parent.name)
    node = node.parent

node = san
while node.parent:
    switches_san.append(node.parent.name)
    node = node.parent

# two different approaches
#number_of_switches = len([x for x in switches_you if x not in switches_san]) + len([x for x in switches_san if x not in switches_you])
number_of_switches = len(set(switches_san).difference(switches_you)) + len(set(switches_you).difference(switches_san))
print("Switches from YOU to SAN:", number_of_switches)