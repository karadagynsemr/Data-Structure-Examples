class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.counter = 0

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left=BST(data)

        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BST(data)
            
    def search(self,data):

        if self.key == data:
            print("Node is found!!")
            return
        if data < self.key:
            if self.left is not None:
                self.left.search(data)
            else:
                print("Not found")

        else:
            if self.right is not None:
                self.right.search(data)

            else:
                print("Not found")     


    def find_min(self):
        if self.left is None:
            return self.key
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.key
        return self.right.find_max()

    def preOrder(self):
        print(self.key,end=" ")
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()

    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        print(self.key,end=" ")
        if self.right is not None:
            self.right.inOrder()

    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.key, end=" ")

    def calculate_element(self):
        if self.key is not None:
            self.counter +=1
        if self.left is not None:
            self.counter += self.left.calculate_element()
        if self.right is not None:
            self.counter += self.right.calculate_element()
        return self.counter


     
        



root = BST(10)

numbers = [3,2,43,12,65,89,31,64,1,5]
for i in numbers:
    root.insert(i)



# BST'deki minimum ve maksimum değerleri bulun ve yazdırın
# print("Minimum value: ", root.find_min())
# print("Maximum value: ", root.find_max())


# root.search(7)
# print("Pre-Order")
# root.preOrder()
# print()
# print("In-Order")
# root.inOrder()
# print()
# print("Post-Order")
# root.postOrder()

print(root.calculate_element())




    


        
       











  
      






