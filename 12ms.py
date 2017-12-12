#Millisecond 12
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/12input.txt", 'r')


#Millisecond 12: First half
class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []
        self.__parents = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def parents(self):
        return self.__parents

    @property
    def children(self):
        return self.__children

    def add_child(self, child):
        self.__children.append(child)

    def add_parent(self, parent):
        self.__parents.append(parent)

class Tree:
    def __init__(self):
        self.__nodes = {}
        self.__root = None

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, node, parent=None):
        if node.identifier == "0": self.__root = node
        self[node.identifier] = node
        if parent is not None:
            parent.add_child(node)
            node.add_parent(parent)

    def remove_node(self, node):
        self.__nodes.pop(node.identifier)

    def getroot(self):
        return self.__root

    def setroot(self, root):
        self.__root = root

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item

programs = Tree()

#add all programs
for line in file: programs.add_node(Node(line.strip().split(' ')[0]))

#reset file
file.seek(0)

#linking parent to child
for line in file:
    line_elem = line.strip().split(' ')
    if len(line_elem) > 2:
        parent_identifier = line_elem[0]

        node_identifiers = [elem.replace(',', '') for elem in line_elem[2:]]
        for node_identifier in node_identifiers:
            programs.add_node(programs[node_identifier], programs[parent_identifier])


#Millisecond 12: First half
already_counted = []
def walk(node):
    if node not in already_counted:
        already_counted.append(node)

        for child in node.children:
            walk(child)

#walk root and walk through all connected children
walk(programs.getroot())
print(len(already_counted))


#Millisecond 12: Second halfs
groups = 0
#run till no nodes are left
while programs.nodes:
    #clear group list
    already_counted.clear()
    #walk through nodegroup of first node still available
    walk(list(programs.nodes.values())[0])
    #remove nodegroup from nodes
    for node in already_counted:
        programs.remove_node(node)
    groups += 1

print(groups)
