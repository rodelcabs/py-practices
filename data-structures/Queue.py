from Stack import Stack

# QUEUE = first in, first out (FIIFO)
class Queue():
    def __init__(self):
        # use stack data structure
        self.queue = Stack()
        

    def enqueue(self, data):
        self.queue.push(data)

    def dequeue(self):
        self.queue.stack = self.queue.stack[1:] # first out always

    def printData(self):
        self.queue.printData()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    queue.printData()
