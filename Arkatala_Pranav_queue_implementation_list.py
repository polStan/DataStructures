class Node:
    def __init__(self, value):
        self.head = value
        self.next = None

class QueueList:
    def __init__(self): # Creates an empty queue using a python list
        print("Initial Queue:")
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item) # the list append method is used to add the item to the queue
        print(f"Enqueued Item: {item}")
    
    def is_empty(self):
        listLen = len(self.queue) # Gets the length of the queue
        if(listLen == 0): # If the length of the queue is 0, then the list is empty
            return True 
        else: # Else, it will return false if the queue is not empty
            return False 
    
    def dequeue(self):
        if not self.is_empty(): # Checks if the queue is empty
            item = self.queue.pop(0) # pops the first item in the begninning of the queue
            print(f"Dequeued Item: {item}") # Prints the dequeued item
            return item # Returns the item that has been dequeued
        else: # Else statement to say that the queue is empty and it will return None
            print("Queue is empty, cannot dequeue.")
            return None
    
    def peek(self): 
        if not self.is_empty(): # checks whether the queue is empty or not
            return self.queue[0] # Returns the top element of the queue
        else: # Else statement to return None
            print("Queue is empty.") 
            return None
    def size(self): # Prints the length of the queue
        print('The length of the queue is: ',len(self.queue))

    def display(self): # Will diplay the items in the queue by a list
        print(f"Queue Items: {self.queue}")

    def print(self): # Prints the elements in the queue
        print(self.queue)

q = QueueList()

q.print()
#enqueue elements to the queue.
q.enqueue(10)
q.enqueue(30)
q.enqueue(90)
q.size()
q.display()
print(f"Front item is: {q.peek()}")
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.size()
q.display()
#dequeue elements from the queue, including testing queue underflow
q.dequeue()

