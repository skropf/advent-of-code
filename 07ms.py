#Millisecond 7
import os

path = os.path.dirname(os.path.realpath(__file__))
file = open(path + "/07input.txt", 'r')


#Millisecond 7: First half
class Node:
    def __init__(self, identifier, weight):
        self.__identifier = identifier
        self.__weight = weight
        self.__children = []
        self.__parent = None

    @property
    def identifier(self):
        return self.__identifier

    @property
    def weight(self):
        return self.__weight

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    def add_child(self, node):
        self.__children.append(node)

    def add_parent(self, parent):
        self.__parent = parent

    def to_string(self):
        return self.__identifier + " " + str(self.__weight)

class Tree:
    def __init__(self):
        self.__nodes = {}
        self.__root = None

    @property
    def nodes(self):
        return self.__nodes

    def add_node(self, node, parent=None):
        self[node.identifier] = node
        if parent is not None:
            parent.add_child(node)
            node.add_parent(parent)

    def getroot(self):
        if self.__root is None:
            root = []
            for node_identifier in registry.nodes:
                node = registry[node_identifier]
                if node.parent is None:
                    root.append(node)

            if len(root) > 1:
                print("Too many nodes with no parents (^=roots) found! Error in code or data.")
            elif len(root) == 0:
                print("No node with parent (^=root) found! Error in code or data.")
            else:
                self.__root = root[0]

        return self.__root

    def setroot(self, root):
        self.__root = root

    def __getitem__(self, key):
        return self.__nodes[key]

    def __setitem__(self, key, item):
        self.__nodes[key] = item


registry = Tree()

#add all nodes with weights
for line in file: registry.add_node(Node(line.strip().split(' ')[0], int(line.strip().split(' ')[1].replace('(', '').replace(')', ''))))

#reset file
file.seek(0)

#linking parent to child
for line in file:
    line_elem = line.strip().split(' ')
    if len(line_elem) > 2:
        parent_identifier = line_elem[0]

        node_identifiers = [elem.replace(',', '') for elem in line_elem[3:]]
        for node_identifier in node_identifiers:
            registry.add_node(registry[node_identifier], registry[parent_identifier])

#getting root
print(registry.getroot().identifier)

#Millisecond 7: Second half
output = {}
def accumulated_weight(node):
    global weight
    weight += node.weight

    for child in node.children:
        accumulated_weight(child)

def walk(node, parent=None, depth=0):
    global weight
    weight = 0
    accumulated_weight(node)

    output[node.identifier] = {"depth": depth, "weight": weight, "parent": parent, "children": node.children}

    for child in node.children:
        walk(child, output[node.identifier], depth + 1)

def find_error(children, parent=None, correct_weight = 0):
    node_identifiers = [node.identifier for node in children]
    nodes = {identifier: output[identifier]["weight"] for identifier in node_identifiers}
    weights = {list(nodes.values()).count(i):i for i in nodes.values()}

    if len(weights) == 1:
        node_weight = registry[[key for key in output.keys() if output[key] is parent][0]].weight

        if correct_weight > parent["weight"]:
            print(node_weight + correct_weight - parent["weight"])
        else:
            print(node_weight - (parent["weight"] - correct_weight))
    elif len(weights) == 2:
        error_weight = weights[1]
        correct_weight = [weight for weight in weights.values() if weight != error_weight][0]
        error_node_identifier = [identifier for identifier in nodes if nodes[identifier] == error_weight][0]

        find_error(output[error_node_identifier]["children"], output[error_node_identifier], correct_weight)


walk(registry.getroot(), None)

find_error(output[next(iter(output))]["children"])
#for entry in output.values():
    #if entry["depth"] == 2: print(entry)
