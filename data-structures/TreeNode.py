from _typeshed import OpenBinaryMode
from Stack import Stack

class TreeNode():
    def __init__(self, data):
        self.parent = None
        self.data = data 
        self.children = Stack()
    
    def addChildren(self, *nodes): 
        self.children.pushAll(*nodes)
    
    def getChildren(self):
        return [node.data for node in self.children.values()]
    
    def treeVisual(self):
        if not bool(self.data):
            return
        
        current = self.data

        print(f"root: {current.data}")

        # traverse, check if node has children
        while len(current.children) > 0:
            print(f"node: {current.data}")
            for node in current.children:
                

if __name__ == "__main__":
    root = TreeNode(1)
    rootChildA = TreeNode(2)
    rootChildB = TreeNode(6)
    root.addChildren(rootChildA,rootChildB)
    rootChildren = root.getChildren()

    rootChildA.addChildren(TreeNode(3), TreeNode(4), TreeNode(5))
    rootChildB.addChildren(TreeNode(7), TreeNode(8))
    
    print(rootChildren)
    

