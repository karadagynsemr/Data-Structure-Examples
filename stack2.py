class Stack:
    def __init__(self):
        self.items=[]

    def push(self,x):
        self.items.append(x)

    def is_empty(self):
        len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            self.items.remove(self.items[-1])
        else:
            return "Stack is already empty!!!"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
            


stack = Stack()



while True:
    
    print("Which operation do you want to do ? 1-push 2-pop 3-quit")
    choice = int(input())
    if choice == 1:
        element_to_push = int(input("Enter element to push:"))
        stack.push(element_to_push)
        print(stack.items)
    elif choice==2:
        stack.pop()
        print(stack.items)
    elif choice==3:
        break















