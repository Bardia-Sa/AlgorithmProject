# class Node:
#     def __init__(self):
#         self.parent = None
#         self.right = None
#         self.left = None
#
#
# class Heap:
#     def __init__(self):
#         self.items = []     # int
#         self.length = len(self.items)
#
#     def heapify(self, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < self.length and self.items[left] < self.items[largest]:
#             largest = left
#         if right < self.length and self.items[right] < self.items[largest]:
#             largest = right
#         if largest != i:
#             self.items[i], self.items[largest] = self.items[largest],self.items[i]
#             self.heapify(largest)
#
#     def build_heap(self):
#         start_index = len(self.items) // 2 - 1
#         for i in range(start_index, -1, -1):
#             self.heapify(i)
#
#     def printHeap(self):
#         print("Array representation of Heap is:")
#
#         for i in range(self.length):
#             print(self.items[i], end=" ")
#         print()
#
#     def add(self, item):
#         self.items.append(item)
#     def remove(self, item):
#         pass
# def heapify(arr, N, i):
#
# 	largest = i
# 	l = 2 * i + 1 # left = 2*i + 1
# 	r = 2 * i + 2 # right = 2*i + 2
#
# 	# If left child is larger than root
# 	if l < N and arr[l] > arr[largest]:
# 		largest = l
#
# 	# If right child is larger than largest so far
# 	if r < N and arr[r] > arr[largest]:
# 		largest = r
#
# 	if largest != i:
# 		arr[i], arr[largest] = arr[largest], arr[i]
#
#
# 		heapify(arr, N, largest)
#
# # Function to build a Max-Heap from the given array
#
#
# def buildHeap(arr, N):
#
# 	# Index of last non-leaf node
# 	startIdx = N // 2 - 1
#
#
# 	for i in range(startIdx, -1, -1):
# 		heapify(arr, N, i)
#
#
# def printHeap(arr, N):
# 	print("Array representation of Heap is:")
#
# 	for i in range(N):
# 		print(arr[i], end=" ")
# 	print()
#
#
#
#
#
#
#
# # a = Heap()
#
# # a.add(1)
# # a.add(3)
# # a.add(5)
# # a.add(4)
# # a.add(6)
# # a.add(13)
# # a.add(10)
# # a.add(9)
# # a.add(8)
# # a.add(15)
# # a.add(17)
# # a.build_heap()
# # print(a.items)

# class Heap:
# 	def __init__(self, capacity: int):
# 		self.capacity = capacity
# 		self.storage = [0] * capacity
# 		self.size = 0
#
# 	def get_parent_index(self, index):			# Some helper methods
# 		return (index - 1) // 2
# 	def get_left_child_index(self, index):
# 		return index * 2 + 1
# 	def get_right_child_index(self, index):
# 		return index
# 	def has_parent(self, index):
# 		return self.get_parent_index(index) >= 0
# 	def has_left_child(self, index):
# 		return self.get_left_child_index(index) < self.size
# 	def has_right_child(self, index):
# 		return self.get_right_child_index(index) < self.size
# 	def is_full(self) -> bool:
# 		return self.size == self.capacity
# 	def swap(self, index1, index2):
# 		self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
#
# 	def heapify_up(self, index):
# 		if self.has_parent(index) and self.has_parent(index) > self.storage[index]:
# 			self.swap(self.get_parent_index(index), index)
# 			self.heapify_up(self.get_parent_index(index))
#
# 	def insert(self, data):
# 		if self.is_full():
# 			raise "heap full"
# 		self.storage[self.size] = data
# 		self.size += 1
# 		self.heapify_up(self.size - 1)
#
# 	def heapify_down(self, index):
# 		smallest = index
# 		if self.has_left_child(index) and self.storage[smallest] > self.get_left_child_index(index):
# 			smallest = self.get_left_child_index(index)
# 		if self.has_right_child(index) and self.storage[smallest] > self.get_right_child_index(index):
# 			smallest = self.get_right_child_index(index)
# 		if smallest is not index:
# 			self.swap(index, smallest)
# 			self.heapify_down(smallest)
#
#
# 	def remove_min(self):
# 		if self.size == 0:
# 			raise "heap empty"
# 		data = self.storage[0]
# 		self.storage[0] = self.storage[self.size - 1]
# 		self.size -= 1
# 		self.heapify_down(0)
# 		return data
#
#
# a = Heap(5)
# a.insert(10)
# a.insert(20)
# a.insert(5)
# a.insert(8)
# a.insert(0)
# # a.insert(1)
#
# print(a.storage)
# class Node:
# 	def __init__(self, value):
# 		self.place_in_heap = None
# 		# self.place_in_arr = None
# 		self.parent = None
# 		self.left = None
# 		self.right = None
# 		self.value = value
#
#
# class Heap:
# 	def __init__(self, cap):
# 		self.capacity = cap
# 		self.size = 0
# 		self.heap = [None] * self.capacity
#
# 	def max_heapify(self, node):
# 		if node.left.value <= self.capacity and node.left.value > node.place_in_heap:
# 			largest = node.left.value
# 		else:
# 			largest = node.place_in_heap
# 		if node.right.value <= self.capacity and node.right.value > largest:
# 			largest = node.right.value
# 		if largest is not node.place_in_heap:
# 			self.max_heapify(largest)
# 	def insert(self, value):
# 		node = Node(value)
# 		if self.size == self.capacity:
# 			print("Heap is full")
# 		self.heap[self.size] = node
# 		node.place_in_heap = self.size
# 		self.size += 1
# 		node.parent = node.place_in_heap // 2
# 		node.right = 2 * node.place_in_heap + 2
# 		node.left = 2 * node.place_in_heap + 1
# 		self.max_heapify(node)
#
#
# a1 = Node(12)
# a2 = Node(3)
# a3 = Node(6)
# a4 = Node(10)
# A = Heap(4)
# print(A.heap)

# class Heap:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.items = []
#         self.size = 0
#
#     def left_child(self,i: int) -> int:
#         return 2*i
#     def right_child(self,i: int) -> int:
#         return 2*i + 1
#     def parent(self,i: int) -> int:
#         return i // 2
#
#
#     def max_heapify(self, i: int):
#         left = self.left_child(i)
#         right = self.right_child(i)
#         if left < self.size and self.items[left] > self.items[i]:
#             largest = left
#         else:
#             largest = i
#         if right < self.size and self.items[right] > self.items[largest]:
#             largest = right
#         if largest is not i:
#             self.items[i], self.items[largest] = self.items[largest], self.items[i]
#             self.max_heapify(largest)
#
#         # if self.left_child(i) <= self.capacity and self.left_child(i) > :
#         #     largest = node.left.value
#         # else:
#         #     largest = node.place_in_heap
#         # if node.right.value <= self.capacity and node.right.value > largest:
#         #     largest = node.right.value
#         # if largest is not node.place_in_heap:
#         #     self.max_heapify(largest)
#
#     def insert(self, item: int) -> None:
#         if self.size == self.capacity:
#             print("Heap is full")
#         else:
#             self.items.append(item)
#             self.max_heapify(self.items[self.size])
#             self.size += 1
#
#
#
# heap = Heap(5)
# heap.insert(3)
# heap.insert(7)
# heap.insert(9)
# heap.insert(18)
# heap.insert(0)
# heap.insert(10)
# print(heap.items)

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

class Skill(Enum):
    F = 6
    E = 5
    D = 4
    C = 3
    B = 2
    A = 1


class Intern:
    def __init__(self, name, age, skill: Skill):
        self.name = name
        self.skill = skill
        self.age = age
        self.position = None
        self.score = skill.value + age


class Company:
    def __init__(self, name):
        nullobj = Intern('null', 0, Skill.A)
        self.name = name
        self.heap = [nullobj]
        self.size = 0
        self.interns = Heap(HeapTypes.MAX)
        self.agenda = None

    # def set_agenda(self, skill: Skill, num):
    #     self.agenda = skill.value + num

    def right_intern(self, intern: Intern):
        temp = self.heap.index(intern) * 2 + 1
        return self.heap[temp]

    def left_intern(self, intern: Intern):
        temp = self.heap.index(intern) * 2
        if self.heap[temp]:
            return self.heap[temp]

    def parent_intern(self, intern: Intern):
        temp = self.heap.index(intern) // 2
        return self.heap[temp]

    def min_intern(self, intern: Intern):
        if self.heap.index(self.right_intern(intern)) > self.size:
            return self.right_intern(intern)
        else:
            if self.heap[self.heap.index(self.left_intern(intern))] < self.heap[self.heap.index(self.right_intern(intern))]:
                return self.left_intern(intern)
            else:
                return self.right_intern(intern)

    def shift_down(self, intern: Intern):
        while self.heap.index(self.left_intern(intern)) <= self.size:
            mini = self.min_intern(intern)
            if intern.score > self.mini.score:
                self.heap[self.heap.index(intern)], self.heap[self.heap.index(mini)] = self.heap[self.heap.index(mini)], self.heap[self.heap.index(intern)]
            intern = mini

    def shift_up(self, intern: Intern):
        while (self.heap.index(intern) // 2) > 0:
            if self.heap[self.heap.index(intern)].score < self.heap[self.heap.index(intern) // 2].score:
                self.heap[self.heap.index(intern)], self.heap[self.heap.index(intern) // 2] = self.heap[self.heap.index(intern) // 2], self.heap[self.heap.index(intern)]
        intern = self.heap[self.heap.index(intern) // 2]

    def heapify(self):
        start = len(self.heap) // 2
        starting_node = self.heap[start]
        while self.heap.index(starting_node) >= 0:
            self.shift_down(starting_node)
            start -= 1

    def add_intern(self, intern: Intern):
        self.heap.append(intern)
        self.size += 1
        self.shift_up(self.heap[self.size])






# a = Heap(HeapTypes.MAX)
# a.insert(12)
# a.insert(10)
# print(a.heap)
a = Company('a')
i1 = Intern('bardia', 20, Skill.A)
i2 = Intern('sabet', 21, Skill.C)
i3 = Intern('jav', 27, Skill.A)
i4 = Intern('ali', 23, Skill.F)
i5 = Intern('el', 30, Skill.B)
i6 = Intern('han', 32, Skill.A)
a.add_intern(i1)
a.add_intern(i2)
# a.add_intern(i3)
# a.add_intern(i4)
# a.add_intern(i5)
# a.add_intern(i6)

