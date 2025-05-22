class Node:
    def __init__(self, data):
        self.data = data # Stores the value of the node
        self.next = None # Pointer to the next node which is intitally none
    
class Stack:
    def __init__(self):
        self.top = None # The stack is empty intitially, so the top is None
        
    def push(self, data):
        n_node = Node(data) # Creates a new node with the given data 
        n_node.next = self.top # Makes the new node point to the value that is the current top
        self.top = n_node # Updates the top 

    def is_empty(self):
        return self.top  == None

    def pop(self):
        if self.top:
            p = self.top # this assigns the current top to a variable that is not permanent
            self.top = self.top.next #This updates  the top to the next node of the linked list
            p.next = None #Deallocates the memory of the previous top node
            return p.next
        else:
            return -1 # returns -1 if the linked list is empty
    def peek(self):
        # This if and else statement checks if the stack is empty or not. If not empty, it returns the top element
        if not self.is_empty():
            return self.top.data
        else:
            print("\nThe stack is empty")

    def print_list(self):
        current = self.top
        while current:
            print(current.data, end=" -- ")
            current = current.next

#Creating an empty stack
my_stack = Stack()
my_stack.print_list()
print(my_stack.pop())
my_stack.push(11)
my_stack.push(22)
my_stack.push(33)
my_stack.push(44)
my_stack.print_list()

print("\nTop element is", my_stack.peek())
print("Removing an element")
my_stack.pop()
my_stack.pop()
my_stack.print_list()


print("\nThe top element is", my_stack.peek())

