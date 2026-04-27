class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def empty(self):
        return not self.stack

st = MyStack()
print(st.empty())
st.push(1)
st.push(2)
st.push(3)
print(st.peek())
print(st.pop())
print(st.size())