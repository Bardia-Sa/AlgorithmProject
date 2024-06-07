from enum import Enum
import math


person = ["bardia", "hedie", "mehdi", "ali", "alireza", "reza", "mohsen", "mohammad", "iliya"]
score = [7, 22, 12, 2, 20, 4, 8, 15, 10]    # score is calculated by adding age and exam score
length = len(score)
heap = []
nodes = {}


class MaxMin(Enum):         # for implementing both min and max heap (priority queue)
    max = 1
    min = 2


max_min = MaxMin.max        # this variable is set manually and determines if queue is max or min


class Node:
    
    def __init__(self, person, score, position):
        self.person = person
        self.score = score
        self.position = position


def Heapify(root):
    left = 2 * root
    right = 2 * root + 1
    index = 0
    
    if left <= length:
        
        if right > length:
            nodes = [left, root]
            
        elif right <= length:
            nodes = [left, right, root]
            
        if max_min == MaxMin.max:
            index = max(nodes, key=lambda i: heap[i].score)
            
        elif max_min == MaxMin.min:
            index = min(nodes, key=lambda i: heap[i].score)
            
        if index != root:
            heap[index], heap[root] = heap[root], heap[index]
            heap[index].position = index
            heap[root].position = root
            
            Heapify(index)


def build_heap():
    heap.append(Node(-1, -1, 0))
    for i in range(length):
        node = Node(person[i], score[i], i+1)
        nodes[person[i]] = node
        heap.append(node)
        
    for i in range(math.floor(length/2), 0, -1):
        Heapify(i)


def extract_output():
    global length
    
    if length == 0:
        print("error: heap is empty")
        return False
    
    else:
        output = heap[1]
        heap[1] = heap[length]
        del heap[length]
        length -= 1
        Heapify(1)
        return output


def score_edit(person, score):
    old_score = nodes[person].score
    nodes[person].score = score
    child_index = nodes[person].position

    if max_min == MaxMin.max:
        if score >= old_score:
            parent_index = math.floor(child_index/2)
            while child_index > 1 and heap[parent_index].score < heap[child_index].score:
                heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
                heap[parent_index].position = parent_index
                heap[child_index].position = child_index
                
                child_index = parent_index
                parent_index = math.floor(child_index/2)
                
        elif score < old_score:
            Heapify(child_index)
            
    elif max_min == MaxMin.min:
        if score <= old_score:
            parent_index = math.floor(child_index/2)
            while child_index > 1 and heap[parent_index].score > heap[child_index].score:
                heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
                heap[parent_index].position = parent_index
                heap[child_index].position = child_index
                
                child_index = parent_index
                parent_index = math.floor(child_index/2)
                
        elif score > old_score:
            Heapify(child_index)


def HeapInsert(person, score):
    node = Node(person, score, length+1)
    nodes[person] = node
    heap.append(node)
    score_edit(person, score)


def to_string():
    for i in heap[1:]:
        print(i.person, i.score, i.position)
    print("\n")
        

print("Building Heap...")
build_heap()
to_string()

p = "bardia"
score_edit(p, 3)
print(f"Edited: {p} score to 3")
to_string()

output = extract_output()
print("Output is: ", output.person, output.score)
to_string()

to_insert = "hedie2"
HeapInsert(to_insert, 25)
print(f"Insert {to_insert} (score 25)")
to_string()

