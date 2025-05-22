class Node:
    def __init__(self, value):
        self.head = value
        self.next = None

class Queue:
    def __init__(self): # Creates an empty queue using a python list
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item) # the append method is used to add the item to the 
        print(f"Enqueued: {item}")
    
    def is_empty(self):
        return len(self.queue) == 0

    
    def dequeue(self):
        if self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty, cannot dequeue.")
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None
    def size(self):
        print('The length of the queue is: ',len(self.queue))

    def display(self):
        print(f"Queue: {self.queue}")

    def print(self):
        print(self.queue)

q = Queue()

q.print()
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

