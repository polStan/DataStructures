class ListNode:
    def __init__(self, data):
        self.data = data  
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None # The head is initially none
        self.tail = None # The tail is intitially none

    def insert_first(self, data):
        new_node = ListNode(data)
        if self.head is None: # Checking if head is empty 
            self.head = new_node # head is updated to point to the new node 
            self.tail = new_node # tail is updated to point to the new node 
        else: # else statement to check if head is not empty
            new_node.next = self.head # the next pointer is updated to point to the head
            self.head.prev = new_node # the previous pointer is updated to point to the new node
            self.head = new_node # the head is updated to point to the new node
    
    def insert_last(self, data):
        new_node = ListNode(data)
        if self.head is None: # checking is head is None
            self.head = new_node # the head points to the new node
            return
        tail = self.head # Head points to the last element in the linked list
        while tail.next: # while loop to link the next element to the last element of the linked list
            tail = tail.next
        tail.next = new_node # updates last elements next to point to the new node
        new_node.prev = tail # updates new nodes previous to the last element of the doubly linked list

    def delete_node(self, key):
        current = self.head # current is pointing to the head
        while current:# While loop to delete node
            if current.data == key: # If statement to check whether the data is equal to the key that is being checked
                if current.prev:# If statement to check whether the prev elements next is pointing to the next of the current element
                    current.prev.next = current.next # If statement to see whether the next elements previous is pointing to the prev node of the current element
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def search_node(self, data):
        current = self.head
        while current is not None: # While loop to check if current doesn't not have empty data
            if current.data == data: # If the  current data that is in the list equals to the the data that is inputed , it returns True
                return True
            current = current.next
        return False # It will return false otherwise

    def insert_after(self, key, data):
        current = self.head # the current is pointing to the head
        while current: # while loop to insert after a given element
            if current.data == key:  # If statement to check if the data is equal to the key that is being searched
                new_node = ListNode(data) # creates a list node containing that data
                new_node.next = current.next # New nodes next pointer is updated to point to the next element 
                new_node.prev = current # The prev pointer is updated to point to the current 
                if current.next: # If statement to check if the next element exists
                    current.next.prev = new_node # The current elements 
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                return
            current = current.next
    
    def length(self): # Checks for the length of the doubly linked list
        count = 0 # count is initially zero
        current = self.head # current is pointing to the first node of the list
        while current: 
            count += 1
            current = current.next
        return count

    def reverse(self):
        current = self.head
        prev = None
        while current:
            prev = current.prev # the prev elemenent is updated to point to the current nodes previous
            current.prev = current.next # The current elements previous pointer is updated to point to the current nodes next
            current.next = prev # updates the current node to point to the previous node
            current = current.prev # Moves the current pointeer to the previous node in the list
        if prev:
            self.head, self.tail = self.tail, self.head # the tail and head are switched
            self.tail.next = None # The next is assigned to None 
            self.head = prev.prev # updates the Head pointer to point to the node before the previous node  
    
    def remove_duplicates(self):
        current = self.head
        seen = set() # Using set because set doesn't allow duplicates
        while current: # Iterating through the DLL
            if current.data in seen: # Checks if the data already exists 
                if current.prev: # checks if a node has a previous node
                    current.prev.next = current.next # the previous nodes next is updated to point to the current elements next
                if current.next: # checks of the node has a next node 
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
            else:
                seen.add(current.data)
            current = current.next

    def rotate(self, n): # rotates the elements
        if self.head is None or n == 0:
            return
        length = self.length()
        n = n % length
        if n == 0:
            return
        current = self.head
        count = 1
        while count < n and current:
            current = current.next
            count += 1
        nth_node = current
        while current.next:
            current = current.next
        current.next = self.head
        self.head.prev = current
        self.head = nth_node.next
        self.head.prev = None
        nth_node.next = None
        self.tail = nth_node
    
    def display(self): # Displays the element in the doubly linked list
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

dll = DoublyLinkedList()
#insert first
print("Before insert_first:")
print(dll.display())
print("insert_first 8")
dll.insert_first(8)
print("insert_first 10")
dll.insert_first(10)
print("insert_first 12")
dll.insert_first(12)
print("insert_first 14")
dll.insert_first(14)
print("insert_first 14")
dll.insert_first(14)
print("After all insert_first:")
print(dll.display())

#insert last
print("\nBefore insert_last:")
print(dll.display())
print("insert_last 6")
dll.insert_last(6)
print("insert_last 4")
dll.insert_last(4)
print("insert_last 2")
dll.insert_last(2)
print("insert_last 0")
dll.insert_last(0)
print("insert_last 0")
dll.insert_last(0)
print("After all insert_last:")
print(dll.display())

#delete node
print("\nBefore deleting nodes:")
print(dll.display())
print("delete_node 10")
dll.delete_node(10)
print("delete_node 12")
dll.delete_node(12)
print("delete_node 16")
dll.delete_node(16)
print("After all delete_node:")
print(dll.display())

#search node
print("\nsearch node")
print("Search Node with 14 found:", dll.search_node(14))
print("Search Node with 100 found:", dll.search_node(100))

#insert after
print("\nBefore inserting nodes:")
print(dll.display())
print("insert 20 after 4")
dll.insert_after(4, 20)
print(dll.display())
print("insert 30 after 2")
dll.insert_after(2,30)
print(dll.display())
print("insert 36 after 100")
dll.insert_after(100,36)
print(dll.display())

#length
print("\nLength of DLL")
print(dll.length())

#Reverse
print("\nLL before reverse")
print(dll.display())
dll.reverse()
print("LL after reverse")
print(dll.display())

#remove_duplicates
print("\nDLL before removing duplicates")
print(dll.display())
dll.remove_duplicates()
print("DLL after removing duplicates")
print(dll.display())

#rotate
print("\nDLL before rotate")
print(dll.display())
dll.rotate(2)
print("DLL after rotate")
print(dll.display())

