class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None     

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node  
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_at_middle(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head
            length = 0
        while current is not None:
            current = current.next
            length += 1

        if length % 2 == 0:
            count = length // 2
        
        else:
            count = (length + 1) // 2
        current = self.head

        while count > 1:
            current = current.next
            count -= 1
        
        new_node.next = current.next
        current.next = self.head
    
    def delete_by_key(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None

        while current and current.data != data:
            prev = current
            current = current.next
            if current is None:
                print(f"The node with value {data} is not found")
                return
            prev.next = current.next
            current = None
    
    def display(self):
        current = self.head
        while current:
            print(current.data,  end ="-->")
            current = current.next
        print("None")

sll = SinglyLinkedList()
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
sll.insert_at_end(6)
sll.display()
      


    

    