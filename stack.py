class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.remove(self.items[-1])
        else:
            return "Stack is already empty!!!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty!!!")
            return None

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Original stack:", stack.items)

stack.push(5)
stack.push(6)

print("After push operations:", stack.items)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print("After pop operations:", stack.items)

print("Top value of stack:", stack.peek())
