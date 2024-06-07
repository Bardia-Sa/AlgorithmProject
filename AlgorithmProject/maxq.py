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
        self.name = name
        self.heap = [0]
        self.size = 0
        self.interns = Heap(HeapTypes.MAX)
        self.agenda = None


    # def set_agenda(self, skill: Skill, num):
    #     self.agenda = skill.value + num


    def right_intern(self, intern: Intern) -> Intern:
        temp = self.heap.index(intern) * 2 + 1
        return self.heap[temp]

    def left_intern(self, intern: Intern):
        temp = self.heap.index(intern) * 2
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

    def heapify(self):
        start = len(self.heap) // 2
        starting_node = self.heap[start]
        while starting_node >= 0:
            self.shift_down(starting_node)
            start -= 1

    def add_intern(self, intern: Intern):
        self.heap.append(intern)
        self.size += 1
        self.heapify()



#
#
#
# a = Company('a')
# i1 = Intern('bardia', 20, Skill.A)
# i2 = Intern('sabet', 21, Skill.C)
# i3 = Intern('javad', 27, Skill.A)
# i4 = Intern('ali', 23, Skill.F)
# i5 = Intern('zizi', 30, Skill.B)
# i6 = Intern('han', 32, Skill.A)
# a.add_intern(i1)
# a.add_intern(i2)
# a.add_intern(i3)
# a.add_intern(i4)
# a.add_intern(i5)
# a.add_intern(i6)




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



