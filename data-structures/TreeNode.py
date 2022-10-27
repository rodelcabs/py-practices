
class TreeNode():
    def __init__(self, data):
        self.parent = None
        self.data = data 
        self.left = None
        self.right = None
    
    # left -> root -> right
    def inOrderTraversal (self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left) # left
            res.append(root.data) # root 
            res = res + self.inOrderTraversal(root.right) # right
        
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    
    print(root.inOrderTraversal(root))
    

