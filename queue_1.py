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


q1=queue()

q1.enqueue(0)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.enqueue(7)
q1.enqueue(8)
q1.enqueue(9)
q1.enqueue(10)


print("Queue aftee enqueue operations :",q1.items)

q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()

print("Queue aftee dequeue operations :",q1.items)


