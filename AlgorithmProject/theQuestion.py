import math
from enum import Enum


class Skills(Enum):
    A = 5
    B = 7
    C = 10
    D = 12
    E = 15
    F = 20


class Node:
    def __init__(self, age, name, position=None):
        self.age = age
        self.name = name
        self.skill = None
        self.all_skills = {'A': 5, 'B': 7, 'C': 10, 'D': 12, 'E': 15, 'F': 20}      # The lower, the better

    def get_score(self):

        return self.skill.value + self.age  # The lower the score, the better

    def set_skill(self, skill: Skills):
        self.skill = skill


class Maxq:
    def __init__(self, initial_nodes):
        self.initial_Nodes = initial_nodes
        self.length = len(self.initial_Nodes)
        self.heap = []
        self.nodes = {}
        self.null_node = Node(None, None, None)

    def get_left_index(self, node) -> int:
        return self.heap.index(node) * 2 + 1

    def get_right_index(self, node) -> int:
        return self.heap.index(node) * 2 + 2

    def get_parent_index(self, node) -> int:
        return self.heap.index(node) // 2

    def get_left_node(self, node):
        try:
            return self.heap[self.heap.index(node) * 2 + 1]
        except:
            return self.null_node

    def get_right_node(self, node):
        try:
            return self.heap[self.heap.index(node) * 2 + 2]
        except:
            return self.null_node

    def get_parent_node(self, node):
        try:
            return self.heap[self.heap.index(node) // 2]
        except:
            return self.null_node

    def set_initial_nodes_as_heap(self):
        self.heap = self.initial_Nodes

    def max_child_node(self, node):             # returns the person with the worst score
        if self.get_right_node(node) is None:
            print('did not have right node')
            return self.get_left_node(node)
        else:
            # if self.heap[self.heap.index(self.get_left_node(node))].score < self.heap[self.heap.index(self.get_right_node(node))].score:
            if self.get_left_node(node).get_score() < self.get_right_node(node).get_score():
                # return self.heap[self.heap.index(self.get_right_node(node))]
                return self.get_right_node(node)
            else:
                # return self.heap[self.heap.index(self.get_left_node(node))]
                return self.get_left_node(node)


    def heapify(self, root):
        pass


a = Node(25, 'bardia')
a.set_skill(Skills.A)
b = Node(18, 'ali')
b.set_skill(Skills.B)
c = Node(18, 'mohsen')
c.set_skill(Skills.A)
d = Node(34, 'sabet')
d.set_skill(Skills.D)
e = Node(10, 'majid')
e.set_skill(Skills.B)
f = Node(29, 'alireza')
f.set_skill(Skills.C)
g = Node(23, 'ele')
g.set_skill(Skills.F)
h = Node(15, 'cube')
h.set_skill(Skills.F)
initial = [a,b,c,d,e,f,g,h]
the_queue = Maxq(initial)
the_queue.set_initial_nodes_as_heap()
# print(the_queue.get_right_node(f).name)
print(the_queue.max_child_node(a).name)






