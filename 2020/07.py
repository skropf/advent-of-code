
fh = open('07.input', 'r')
puzzle = fh.readlines()


### classes & functions ###
class Node:
    def __init__(self, parent, name, amount):
        self.parent = parent
        self.children = []
        self.name = name
        self.amount = amount

    def add_child(self, node): self.children.append(node)

class Tree:
    root = None

    def __init__(self, raw_rules):
        self.fill_tree(raw_rules)

    def search_name_in_tree_nodes(self, name, node):
        if not node: return
        for child in node.children:
            self.search_name_in_tree_nodes(name, child)
        if node.name == name: return node

    def fill_tree(self, raw_rules):
        bag_rules = []
        for rule in raw_rules:
            bags = rule.split(' contain ')
            main_bag = bags[0]
    
            bag_rules.append((main_bag, get_bag_rules(bags[1])))

        i = 0
        while bag_rules:
            if i >= len(bag_rules): i = 0
            bag = bag_rules[i]
            name = bag[0]
            
            if not self.root: self.root = Node(None, name, 1)
            node = self.search_name_in_tree_nodes(name, self.root)

            if node:
                if node.children: print("children already here! why?")

                for name, amount in bag[1]:
                    new_node = Node(node, name, amount)
                    node.add_child(new_node)
                
                bag_rules.remove(bag_rules[0])
                i = 0
            else:
                i += 1
                continue
            


    def count_shiny_gold_container(self):
        nr_of_shiny_gold_bags = 0

        

        return nr_of_shiny_gold_bags


def get_bag_rules(rules):
    bag_rules = []
    rules = rules.replace(".", '')
    rules = rules.replace("\n", '')

    if ", " in rules:
        rules = rules.split(", ")
        for rule in rules:
            amount, bag = rule.split(' ', 1)
            bag_rules.append((bag, amount))
    else:
        if not "no other bags" in rules:
            amount, bag = rules.split(' ', 1)
            bag_rules.append((bag, amount))

    return bag_rules
### /classes & functions ###


tree = Tree(puzzle)

print("Part 1:", str(count_shiny_gold_container()))
        
        



