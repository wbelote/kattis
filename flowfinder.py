import sys, functools

class Node:
    def __init__(self):
        self.parent = None
        self.children = []
        self.known = None
        self.value = 0

    def __add__(self, other):
        return self.value + other.value

    def __int__(self):
        return self.value


def node_sum(nodes):
    total = 0
    for i in range(len(nodes)):
        total += nodes[i].value
    return total

def reconstruct_node(node, debug=False):    
    children_known = True
    for child in node.children:
        if not child.known:
            children_known = False
            break

    if children_known:
        node.value = node_sum(node.children)
        node.known = True
        return True

    if not node.parent.known:
        return False
    siblings_known = True
    for sibling in node.parent.children:
        if sibling != node and not sibling.known:
            siblings_known = False
            break
        
    if siblings_known:
        print(node.parent.value, node_sum(node.parent.children))
        node.value = node.parent.value - node_sum(node.parent.children)
        node.known = True
        return True
    return False


def main():
    num_nodes = int(sys.stdin.readline())
    nodes = [Node() for _ in range(num_nodes)]

    node_connections = [int(x) for x in sys.stdin.readline().split()]
    node_vals = [int(x) for x in sys.stdin.readline().split()]

    unknown = []

    for i in range(num_nodes):
        node = nodes[i]
        if i:
            node.parent = nodes[node_connections[i - 1] - 1]
            node.parent.children.append(node)

        node.value = node_vals[i]
        if node.value:
            node.known = True
        else:
            unknown.append(i)

    learned = True
    while learned:
        learned = False
        for i in range(len(unknown), 0, -1):
            node = nodes[unknown[i - 1]]
            if reconstruct_node(node, i==2):
                unknown.pop(i - 1)
                learned = True

    if len(unknown) > 0:
        print("impossible")
    else:
        print_tree(nodes[0])

def print_tree(node):
    print(str(node.value), end=" ")
    for child in node.children:
        print_tree(child)


main()
