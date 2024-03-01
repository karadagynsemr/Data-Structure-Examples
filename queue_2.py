class queue:
  
    def __init__(self):
        self.items=[]
        self.head=0
        self.back=0
 
    def is_full(self):
        return len(self.items) == 10
    
    def is_empty(self):
        return len(self.items) ==0
        
    def enqueue(self,x):
        if not self.is_full():
            self.items.append(x)
            self.head=self.items[0]
            self.back=x
        else:
            print("Queue is full you can't add" , x)
        
    def dequeue(self):
        if not self.is_empty():
            self.items.remove(self.head)
            if not self.is_empty():
              self.head=self.items[0]
        else:
            print("Queue is empty!!!") 
            

q1 = queue()

while True:
    choice = int(input(print("Choose your operation (1-add 2-remove 3-show 4-quit):")))
    if choice == 1:
        value = int(input("Enter value to add queue:"))
        q1.enqueue(value)
    elif choice == 2:
        q1.dequeue()
    elif choice == 3:
        print(q1.items)
    elif choice == 4:
        break
    else:
        print("Enter correct operation!!!")