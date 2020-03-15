# STack ADT
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Queue ADT
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# STack ADT operation example
s=Stack()

print('Stack operation examples')
print(s.isEmpty())
s.push(5)
s.push('python')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(11.5)
print(s.pop())
print(s.pop())
print(s.size())


# Queue ADT operation example
q=Queue()

print('Queue operation examples')
print(q.isEmpty())
q.enqueue(5)
q.enqueue('python')
print(q.front())
q.enqueue(True)
print(q.size())
print(q.isEmpty())
q.enqueue(11.5)
print(q.dequeue())
print(q.dequeue())
print(q.size())