from Node import Node

# STACK = Last in, first out (LIFO)
class Stack:
    def __init__ (self):
        self.stack = []
        self.size = 0

    def push(self, data):
        newData = Node(data)
        self.stack.append(newData)
        self.increment()

    def pop(self):
        if self.size == 0:
            return 

        self.decrement()
        self.stack = self.stack[:self.size]
        

    def increment(self):
        self.size+=1
    
    def decrement(self):
        self.size-=1

    def printData(self):
        print([i.data for i in self.stack])


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.printData()
