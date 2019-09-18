"""
combinations(node):
    combinations(right)
    * combinations(left)
    * triangle(count(right), count(left))

triangle(a, b):
    a+b C a
"""

import sys
from math import factorial as fact


def merge(a, b):
    return fact(a + b) // (fact(a) * fact(b))


class Tree:
    def __init__(self, head=None):
        self.head = head
        if self.head is None:
            self.left = None
            self.right = None
        else:
            self.left = Tree()
            self.right = Tree()

    def insert(self, val):
        if self.head is None:
            self.head = val
            self.left = Tree()
            self.right = Tree()
        elif val < self.head:
            self.left.insert(val)
        else:
            self.right.insert(val)

    def __len__(self):
        if self.head is None:
            return 0
        return len(self.left) + len(self.right) + 1

    def combinations(self):
        if self.head is None:
            return 1

        l_com = self.left.combinations()
        r_com = self.right.combinations()
        m_com = merge(len(self.right), len(self.left))
        return l_com * r_com * m_com


def main():
    n = int(sys.stdin.readline())
    while n:
        tree = Tree()
        for val in sys.stdin.readline().split():
            tree.insert(int(val))
        print(tree.combinations())
        n = int(sys.stdin.readline())


main()
