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
        if self.root is None: # checks if the root is None
            self.root = new_node # the root becomes the new node
            return
        current = self.root 
        parent = current

        while current is not None: # Checks if current is not none
            parent = current
            if val < current.val: # Checks if current value is greater than the val that that is being checked
                current = current.left
            else:
                current = current.right
        if val < parent.val: # Checks if the value is less then the parent node
            parent.left = new_node # Moves to the left child
        else:
            parent.right = new_node # moves to the right child
        
    
    def search(self, val):
        current = self.root
        while current:
            if val == current.val: # If the value is equal to the current valuee then it returns true
                return True
            elif val < current.val: #If the value that is being checked is less than the current val
                current = current.left # current pointer moves to the left 
            else:
                current = current.right # current pointer moves to the right
        return False
    
    def delete(self, val):
        parent = None
        current = self.root

        while current and current.val != val:
            parent = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        if current is None:  # Node not found
            return self.root

        # Case 1: Node has no children
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: Node has two children
        elif current.left and current.right:
            successor = self.get_minimum_node(current.right)
            val = successor.value
            self.delete(successor.value)
            current.value = val

        # Case 3: Node has one child
        else:
            if current.left:
                child = current.left
            else:
                child = current.right

            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

        return self.root
    
    def get_minimum_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Returns: A list of integers representing an in-order traversal of the BST.
    # Description: Performs an in-order traversal (left-root-right) and returns the values in sorted order.
    def inorder_traversal(self):
        result = []
        stack = [] #stack to keep track of the nodes.
        current = self.root

        while current or stack:
            # Reach the leftmost Node of the current Node
            while current:
                stack.append(current)
                current = current.left #traverse the left subtree by pushing nodes onto the stack.
        
            # Current must be None at this point
            current = stack.pop() # When we reach a leaf, we pop nodes from the stack and add their values to the result.
            result.append(current.val)  # Visit the node
            current = current.right  # Visit the right subtree

        return result
    
    # Returns: A list of integers representing a pre-order traversal of the BST.
    # Description: Performs a pre-order traversal (root-left-right) and returns the values.
    def preorder_traversal(self):
        if self.root is None:
            return []

        stack = [self.root]
        result = []

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)      # Visit the node
                stack.append(node.right)     # Push right child to stack (if it exists)
                stack.append(node.left)      # Push left child to stack (if it exists)

        return result
    
    # Returns: A list of integers representing a post-order traversal of the BST.
    # Description: Performs a post-order traversal (left-right-root) and returns the values
    def postorder_traversal(self):
        if self.root is None:
            return []
        stack1 = [self.root] # First stack is used for processing nodes
        stack2 = [] # Second stack is used for postorder sequence
        result = [] # stores the elements in an array
        # traverses the tree in a way that reverses postorder by visiting the root first and moving to left and right children.
        while stack1:
            node = stack1.pop()
            stack2.append(node)
        
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
    
        # Collecting nodes in postorder
        # After processing all nodes, it reverses the order by popping nodes from stack2 and adds their values to the result.
        while stack2:
            node = stack2.pop()
            result.append(node.val)
    
        return result
        
bst = BinarySearchTree()
bst.insert(20)
bst.insert(15)
bst.insert(17)
bst.insert(10)
bst.insert(11)
bst.insert(13)
bst.insert(12)
bst.insert(24)
bst.insert(56)
bst.insert(90)

print("Searching for element 24:", bst.search(24))
print("Searching for element 22:", bst.search(22))
print("Searching for element 56:", bst.search(56))
print("Searching for element 90:", bst.search(90))

bst.delete(24)

rst = bst.preorder_traversal()
print("PreOrder:", rst)
rst = bst.inorder_traversal()
print("InOrder:", rst)
rst = bst.postorder_traversal()
print("PostOrder:", rst)


    

