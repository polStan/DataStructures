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
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node

    def delete_first(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
        else:
            next_node = self.head.next
            prev_node = self.head.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            self.head = next_node
        
    
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
        else: 
            last_node = self.head.prev
            prev_node = last_node.prev
            prev_node.next = self.head
            self.head.prev = prev_node
    
    def display(self): # displays the circular doubly linked list
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print()

        
        
circular_doubly_list = CircularDoublyLinkedList()
circular_doubly_list.insert_first(10)
circular_doubly_list.insert_first(20)
circular_doubly_list.insert_first(30)
circular_doubly_list.insert_first(50)
circular_doubly_list.insert_last(5)

# Display list in forward and backward directions
circular_doubly_list.delete_first()
circular_doubly_list.delete_last()
circular_doubly_list.display()

