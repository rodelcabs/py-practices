
# STACK = Last in, first out (LIFO)
class Stack:
    def __init__ (self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.increment()

    def pushAll(self, *args):
        return [self.push(i) for i in args]

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
        print(self.stack)
    
    def values (self):
        return self.stack


if __name__ == "__main__":
    stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.pop()
    stack.pushAll(1,2,3,4) 
    stack.printData()
