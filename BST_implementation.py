class TreeNode:
    def __init__(self, val):
       self.left = None
       self.right = None
       self.val = val

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        parent = current

        while current is not None:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        
    
    def search(self, val):
        if self.root is None:
            return False
        if self.root.val == val:
            return True
        if val < self.root.val:
            return self.root.left
        else:
            return self.root.right
        

        


    def delete(self, val):
        pass
            
       
    


    def inorder_traversal(self):
        pass
    
    def preorder_traversal(self):
        pass

    def postorder_traversal(self):
        pass



    

bst = BinarySearchTree()
bst.insert(20)
bst.insert(15)
bst.insert(17)
bst.insert(10)
bst.insert(11)
bst.insert(13)
bst.insert(12)
print("Inorder Traversal: ",bst.inorder_traversal())
print("Postorder Traversal: ",bst.postorder_traversal())
print("Preorder Traversal: ",bst.preorder_traversal())
    

