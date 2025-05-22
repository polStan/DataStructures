class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data): # The node is inserted at the beginning of the circular singly linked list 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head: 
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_last(self, data): # The node is inserted at the end of the circular singly linked list 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def delete_first(self): # deletes the 1st  node at the beginning of the circular singly linked list  
        if self.head is None: 
            print("The list is empty!")
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next

    
    def delete_last(self): # Deletes the last node if the node exists
        if self.head is None:
            print("The list is empty!")
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        current.next = self.head
    
    def display(self): # displays the circular singly linked list
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

        

# Main function
circular_list = CircularSinglyLinkedList()
circular_list.insert_first(10)
circular_list.insert_first(20)
circular_list.insert_first(30)
circular_list.insert_first(40)
circular_list.insert_first(50)
circular_list.insert_last(60)
circular_list.insert_last(70)
circular_list.delete_first()
circular_list.delete_last()
circular_list.display()

