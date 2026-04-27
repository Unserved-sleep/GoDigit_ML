class MyQueue:
    def __init__(self):
        self.items = []
    def empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)

qu = MyQueue()
print(qu.empty())
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
print(qu.peek())
print(qu.dequeue())
print(qu.size())