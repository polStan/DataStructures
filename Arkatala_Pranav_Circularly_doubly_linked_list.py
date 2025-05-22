class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        if not self.head: # checking if head doesn't exit
            self.head = new_node  # head pointer points to new node
            self.head.next = self.head # the next pointer points to head
            self.head.prev = self.head # The prev pointer is updated to point to head
        else:
            tail = self.head.prev 
            new_node.next = self.head  
            new_node.prev = tail 
            self.head.prev = new_node 
            tail.next = new_node 
            self.head = new_node 
    
    def insert_last(self, data): # inserts node at the end of the list
        new_node = Node(data)
        if self.head is None: # When the linked list is empty
            self.head = new_node 
            self.head.next =self.head
            self.head.prev = self.head
        else: # When there exists a node
            tail = self.head
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def delete_first(self): # Deletes the node in the beginning of the list
        if self.head is None:
            return
        if self.head.next == self.head: # when the linked list is empty
            self.head = None
        else: # when there exists a node
            tail = self.head.prev
            next_node = self.head.next
            next_node.prev = tail
            tail.next = next_node
            self.head = next_node
        
    def delete_last(self): # Deletes the node at the end of the list 
        if self.head is None:
            return  
        if self.head.next == self.head:
            self.head = None

        else: # when there exists a node
            tail = self.head.prev
            prev_node = tail.prev
            prev_node.next = self.head
            self.head.prev = prev_node

        
        

    def display_forward(self): 
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end= '<-->')
            current = current.next
            if current == self.head:
                break
        print("(tail)")


cdll = CircularDoublyLinkedList()
cdll.insert_first(9)
cdll.insert_first(8)
cdll.insert_first(7)
cdll.insert_first(6)
cdll.display_forward()
cdll.insert_last(10)
cdll.insert_last(11)
cdll.insert_last(12)
cdll.insert_last(13)
cdll.display_forward()
cdll.delete_first()
cdll.display_forward()
cdll.delete_last()
cdll.delete_last()
cdll.delete_last()
cdll.delete_last()
cdll.delete_last()
cdll.delete_last()
cdll.delete_last()
cdll.display_forward()