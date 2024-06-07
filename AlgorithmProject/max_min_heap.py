from enum import Enum


class HeapTypes(Enum):
    MIN = "min heap"
    MAX = "max heap"


class Heap:
    def __init__(self, heap_type: HeapTypes):
        self.heap = [0]
        self.size = 0
        self.heap_type = heap_type

    def left_child(self, index) -> int:
        return 2 * index

    def right_child(self, index) -> int:
        return 2 * index + 1

    def parent(self, index) -> int:
        return index // 2

    def max_child(self, index) -> int:
        if self.right_child(index) > self.size:
            return self.left_child(index)
        else:
            if self.heap[self.left_child(index)] < self.heap[self.right_child(index)]:
                return self.right_child(index)
            else:
                return self.left_child(index)

    def min_child(self, index) -> int:
        if self.right_child(index) > self.size:
            return self.left_child(index)
        else:
            if self.heap[self.left_child(index)] < self.heap[self.right_child(index)]:
                return self.left_child(index)
            else:
                return self.right_child(index)

    def shift_up(self, index):
        if self.heap_type == HeapTypes.MIN:
            while (index // 2) > 0:                 # while the node has a parent
                if self.heap[index] < self.heap[index // 2]:        # if the node was smaller than its parent, swap
                    self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                index = index // 2
        if self.heap_type == HeapTypes.MAX:
            while (index // 2) > 0:
                if self.heap[index] > self.heap[index // 2]:        # if the node was bigger than its parent, swap
                    self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
                index = index // 2

    def shift_down(self, index):
        if self.heap_type == HeapTypes.MIN:
            while (self.left_child(index)) <= self.size:
                mini = self.min_child(index)
                if self.heap[index] > self.heap[mini]:  # if the current node is bigger than its minimum child then swap
                    self.heap[index], self.heap[mini] = self.heap[mini], self.heap[index]
                index = mini
        if self.heap_type == HeapTypes.MAX:
            while (self.right_child(index)) <= self.size:
                maxi = self.max_child(index)
                if self.heap[index] < self.heap[maxi]:  # if the current node is smaller than its maximum child, swap
                    self.heap[index], self.heap[maxi] = self.heap[maxi], self.heap[index]
                index = maxi

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.shift_up(self.size)

    def delete(self, index) -> int:
        deleted = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shift_down(1)
        return deleted

    def build_heap(self, arr):
        i = len(arr) // 2
        self.size = len(arr)
        self.heap = [0] + arr[:]
        while i > 0:
            self.shift_down(i)
            i = i - 1

    def replace_element(self, value, index):
        current = self.heap[index]
        self.heap[index] = value
        if self.heap_type == HeapTypes.MIN:
            if value > current:
                self.shift_down(index)
            if value < current:
                self.shift_up(index)
        if self.heap_type == HeapTypes.MAX:
            if value > current:
                self.shift_up(index)
            if value < current:
                self.shift_down(index)

    def heapify(self):
        start = len(self.heap) // 2
        while start >= 0:
            self.shift_down(start)
            start -= 1


h = Heap(HeapTypes.MIN)
print('this is a min heap')
print('inserting nodes... ')
h.insert(10)
h.insert(12)
h.insert(8)
h.insert(16)
h.insert(5)
h.insert(21)
h.insert(3)
h.insert(25)
h.insert(10)
h.insert(34)
h.insert(1)
h.insert(45)
print(h.heap)

print('replacing index 1 (value 1) with value 100')
h.replace_element(100, 1)
print(h.heap)

print('deleting index 1')
h.delete(1)
print(h.heap)

print('building min heap from arr in a new heap')
arr = [10, 20, 30, 40, 50, 23, 543, 124, 98]
s = Heap(HeapTypes.MIN)
s.build_heap(arr)
print(s.heap)


print('this is a max heap')
p = Heap(HeapTypes.MAX)
print('inserting nodes... ')
p.insert(10)
p.insert(12)
p.insert(8)
p.insert(16)
p.insert(5)
p.insert(21)
p.insert(3)
p.insert(25)
p.insert(10)
p.insert(34)
p.insert(1)
p.insert(45)
print(p.heap)

