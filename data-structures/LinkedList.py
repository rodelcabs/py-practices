from Node import Node

class LinkedList:
    def __init__ (self):
        self.head = None # this will be the whole linked list object
        self.size = 0

    def insertFirst(self, data):
        self.head = Node(data, self.head)
        self.incrementSize()

    def insertLast(self, data):
        node = Node(data)
        current = None 

        if not bool(self.head):
            self.head = node 
        else:
            current = self.head
            # traverse the list
            while bool(current.next):
                current = current.next

            current.next = node

        self.incrementSize()

    def insertAt (self, index, data):
        if index > self.size:
            return

        if index == 0:
            self.insertFirst(data)
            return 

        node = Node(data)
        curr, prev, count = self.head, None, 0     

        # traverse the list until we reach the desired index
        while count < index:
            prev = curr
            curr = curr.next
            count+=1      

        prev.next = node
        node.next = curr
        self.incrementSize()
        

    def getAt(self, index):
        if index > self.size:
            return

        if index == 0:
            return self.head

        current,c = self.head,0
        
        while c < index:
            current = current.next
            c+=1

        return self.data(current, index)

    def getFirst(self):
        return self.data(self.head)

    def getLast(self):
        if self.size == 0:
            return

        current = self.head

        while bool(current.next):
            current = current.next
        
        return self.data(current, self.size - 1)

    def removeFirst(self): 
        if self.size == 0:
            return

        current = self.head
        self.head = current.next
        self.decrementSize()
    
    def removeLast(self): 
        if self.size == 0:
            return

        current, prev = self.head, None

        while bool(current.next):
            prev = current
            current = current.next
        
        prev.next = None
        self.decrementSize()

    def removeAt(self, index):
        if self.size == 0 or index >= self.size:
            return
        print(self.size)

        current, prev, c = self.head, None, 0

        while c < index:
            prev = current
            current = current.next
            c+=1

        prev.next = current.next if bool(current) else current
        self.decrementSize()
    
    def reverse(self): # the iconic reverse linked list
        current, prev, next = self.head, None, None

        while bool(current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        

    def print(self):
        current, c = self.head, 0
        
        while current:
            print(self.data(current, c))
            current = current.next
            c+=1
    
    def data(self, node, i = None):
        next = node.next.data if bool(node.next) else node.next
        return {'index': i, 'data': node.data, 'next': next }

    def incrementSize(self):
        self.size += 1
    
    def decrementSize(self):
        self.size -= 1


linkedList = LinkedList()
linkedList.insertLast(300)
linkedList.insertFirst(200)
linkedList.insertFirst(100)
linkedList.insertAt(1, 101)
# print(linkedList.getAt(2))
# print(linkedList.getFirst())
# print(linkedList.getLast())
# linkedList.removeFirst()
# linkedList.removeLast()
print("BEFORE")
linkedList.print()
# linkedList.removeAt(1)
# linkedList.removeAt(2)
print("AFTER")
linkedList.reverse()
linkedList.print()

