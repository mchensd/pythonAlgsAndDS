class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setPrev(self, newPrev):
        self.prev = newPrev

class DoublyLinkedList:
    def __init__(self):

        self.none = Node(None)
        self.head = None

    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.head.next = self.none
            self.head.prev = self.none
            self.none.next = self.head
        else:
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            self.head.prev = self.none
            self.none.next = self.head

    def size(self):
        if self.head == None:
            return 0
        counter = 1
        cur_node = self.head
        while cur_node.getNext() != self.none:
            cur_node = cur_node.getNext()
            counter += 1
        return counter

    def search(self, item):
        x = self.none.next
        while x != self.none and x.getData() != item:
            x = x.next
        return False if x == self.none else True

    def remove(self, item):
        current = self.head
        previous = self.head.prev

        while current.getData() != item:
            previous = current
            current = current.getNext()

        if previous == self.none:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

    def index(self, index):
        cur_node = self.head
        i = 0
        while i < index:
            cur_node = cur_node.next()
            if cur_node == self.none:
                return "Index out of range"
            i += 1
        return cur_node.data

class SinglyLinkedList:
    def __init__(self):
        self.none = Node(None)

        self.head = self.none
        self.tail = self.head

        self.none.next = self.head
        self.tail.next = self.none
    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.none.next = self.head

        """temp = Node(item)
        if self.head == None:
            self.head = temp
            self.head.next = self.none
            self.none.next = self.head
            self.tail = self.head
        else:
            temp.next = self.head
            self.head = temp
            self.none.next = self.head
"""
    def remove(self, item):
        cur_node = self.head
        prev_node = self.none
        while cur_node.data != item:
            prev_node = cur_node
            cur_node = cur_node.next
        prev_node.next = cur_node.next
    def size(self):
        if self.head == None:
            return 0
        counter = 1
        cur_node = self.head
        while cur_node.getNext() != self.none:
            cur_node = cur_node.getNext()
            counter += 1
        return counter
    def search(self, item):
        cur_node = self.head
        while cur_node.next != self.none:  # self.head exists and we are not at end of the list

            if cur_node.data == item:
                return True
            cur_node = cur_node.next
        return False

    def index(self, index):
        cur_node = self.head
        i = 0
        while i < index:
            cur_node = cur_node.next
            if cur_node == self.none:
                return "Index out of range"
            i += 1
        return cur_node.data

class Stack:
    def __init__(self):
        self.storage = SinglyLinkedList()

    def push(self, item):
        self.storage.add(item)

    def pop(self):
        return self.storage.head

class Queue:
    def __init__(self):
        self.storage = SinglyLinkedList()

    def enqueue(self, item):
        temp = Node(item)
        self.storage.tail.next = temp
        temp.next = self.storage.none
        self.storage.tail = temp

    def dequeue(self,):
        self.storage.head = self.storage.head.next
        return self.storage.head.data



ul = DoublyLinkedList()
'''
ul.add(56)
ul.add(52)
ul.add(520)
ul.add(132)
ul.add(689)

print(ul.size())
print(ul.search(52))
print(ul.search(2))
print(ul.search(56))
ul.remove(520)
print(ul.search(520))'''

sl = SinglyLinkedList()
sl.add(50)
sl.add(60)
sl.add(70)
sl.add(80)
sl.size()
print(sl.search(70))
sl.remove(70)
print(sl.search(70))
print(sl.index(2))
print(sl.index(0))
print(sl.index(1))

q = Queue()
q.enqueue(5)
q.enqueue(34)
q.enqueue(125)
q.enqueue(1566)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

s2 = SinglyLinkedList()
print(s2.head.next.next.data)