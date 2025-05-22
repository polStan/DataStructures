class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data): # Inserts node at the beginning of the list 
        new_node = Node(data)  

        if not self.head:
            self.head = new_node
            self.head.next  = self.head
        
        else: # when there exists multiple nodes
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
    
    def insert_last(self, data): # Inserts node at the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else: # when there exists multiple nodes
            current = self.head 
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    def delete_first(self): # Deletes first node in the list
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
        else: # when there exists multiple nodes
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        return
    
    def delete_last(self): # Deletes last node in the list
        if self.head is None: # If there is no linked list
            return
        prev = None
        current = self.head
        
        if self.head.next == self.head: # when there is only one node
            current = None
            self.head = None
        else: # when there exists multiple nodes
            prev = current
            current = current.next
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = self.head
                
    def display(self):
        if not self.head:
            print("The list is empty")
            return
        current = self.head
        while True:
            print(current.data, end = "-->")
            current = current.next
            if current == self.head:
                break
        print("(head)")

csll = CircularSinglyLinkedList()
csll.insert_first(6)
csll.insert_first(5)
csll.insert_first(3)
csll.insert_first(2)
csll.display()
csll.insert_last(8)
csll.insert_last(10)
csll.insert_last(11)
csll.insert_last(12)
csll.display()
csll.delete_first()
csll.display()
csll.delete_last()
csll.display()
csll.delete_last()
csll.display()
csll.delete_last()
csll.delete_last()
csll.delete_last()
csll.delete_last()
csll.delete_last()
csll.display()



             