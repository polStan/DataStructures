class Node:
    def __init__(self, data):
        self.data = data # Stores the value of the node
        self.next = None # Pointer to the next node which is initially none

class Queue:
    def __init__(self):
        self.head = None  #The Queue  head is empty initially
        self.tail = None  #The Queue  tail is empty initially
        self.size = 0     #The Queue  size is 0 initially

    def enqueue(self, data):
        new_node = Node(data) # Creates a new node with the given data 
        if self.is_empty():   # Check for size before adding the new node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size = self.size + 1  # Increment the size by 1
        print(f"Enqueued Item: {data}") # display the added item

    def dequeue(self):
        if self.is_empty(): # Check for size before deleting the node
            return None
        data = self.head.data # getting the value of the head to be removed from LinkedList
        self.head = self.head.next # head will point to the next element in the linked list
        self.size = self.size - 1 # Decrements the size by 1
        if self.is_empty():
            self.tail = None
        print(f"Dequeued Item: {data}") # display the deleted item
        return data

    def peek(self):
        if self.is_empty(): # Checks if the linked list is empty or not
            return None
        return self.head.data # It returns the data if there is a top element
    
    def is_empty(self): # Checks if the queue is empty or not
        if self.size == 0:
            return True
        else:
            return False
    
    def display(self): # Displays the queue in a linked list followed by arrows
        if self.is_empty(): # Checks for queue underflow
            print("Queue is empty. queue underflow")
            return
        current = self.head
        print("Queue:", end = " ")
        while current:
            print(current.data, end = "-->")
            current = current.next
        print("None")

#Creating an empty stack
queue = Queue()
#enqueue elements to the queue.
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(1)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(4)
queue.enqueue(7)
queue.enqueue(6)
queue.enqueue(4)
queue.enqueue(20)
queue.display()
#'dequeue' elements from the queue.
queue.dequeue() 
queue.dequeue()   
queue.dequeue() 
queue.dequeue() 
queue.dequeue() 
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(76)
queue.display()
#testing  for queue underflow.
queue.dequeue()
queue.display()
