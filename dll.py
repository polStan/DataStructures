class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:

            new_node.next = self.head   
            self.head.prev = new_node
            self.head = new_node
    
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last =self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_first(self):
        
        if self.head is None:
            return
        
        current = self.head
        self.head = current.next
        current = None
        
    def delete_last(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end= '<-->')
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_first(7)
dll.insert_first(8)
dll.insert_first(8)
dll.insert_last(2)
dll.insert_last(10)
dll.display()
#dll.delete_first()
dll.delete_last()
dll.delete_last()
dll.display()