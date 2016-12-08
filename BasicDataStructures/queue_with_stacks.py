from stack import Stack


class QueueS:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
    def enqueue(self, item):
        self.inbox.push(item)
    def dequeue(self):
        if self.outbox.size() == 0:
            while self.inbox.size() != 0:
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()
    def size(self):
        return self.inbox.size()
    def is_empty(self):
        return self.inbox.isEmpty()

q = QueueS()

for i in range(5):
    q.enqueue(i)


for i in range(2):
    print(q.dequeue())


