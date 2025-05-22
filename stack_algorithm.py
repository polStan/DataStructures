'''class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.stack = []
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
    
    def peek(self):
        if self.is_empty:
            return "Stack is empty, cannot peek"
        
        return self.top.data
    
    def size(self):
        current = self.top
        count = 0
        while current:

            count += 1
            current = current.next
        
        return count

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top element is:", my_stack.peek())
print("Stack size is:", my_stack.size())
print("Popped element is:", my_stack.pop())
print("Stack size after pop is:", my_stack.size())

class Stack:
    def __init__(self):
        self.stack = []
# Push operation (add an element to the stack)
    def push(self, item):
        self.stack.append(item)
# Pop operation (remove and return the top element from the stack)
    def pop(self):
        if self.is_empty():
            return "Stack is empty, cannot pop"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty, cannot peek"
        return self.stack[-1]
# Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
# Return the size of the stack
    def size(self):
        return len(self.stack)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print("Top element:", my_stack.peek()) # Output: 30
print("Stack size:", my_stack.size()) # Output: 3
print("Popped element:", my_stack.pop()) # Output: 30
print("Stack size after pop:", my_stack.size()) # Output: 2'''

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect",browsing_session[-1])
if not browsing_session:
    print("d")