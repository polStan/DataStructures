class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None  # Pointer to the next node

class HashTable:
    def __init__(self, size: int = 10) -> None:
        self.size = size  # size of the hash function
        self.table = [None] * size  # Array of head pointers for linked lists

    # Computes the hash index for a given key using modulo operation. Use key % size. Size should be 10
    def hash_function(self, key: int) -> int:
        return key % self.size  # Hash function

    # Inserts the key into the hash table using head insertion in the linked list.
    def insert(self, key: int) -> None:
        index = self.hash_function(key) # getting the index of the key using hashfunction
        if self.table[index] is None:
            self.table[index] = Node(key) # if there is no key at the index, insert the key into that index
        else:
            current = self.table[index]  # getting the node of the key
            while current:               # iterates through the node next till the end
                if current.next is None: # key not found in current node
                    break
                current = current.next   # goes to next node
            current.next = Node(key)    # if the current node next is null, insert the key

    # Deletes a key from the hash table if it exists
    def delete(self, key: int) -> bool:
        index = self.hash_function(key) # getting the index of the key using hashfunction
        current = self.table[index]     # getting the node of the key
        prev = None

        while current:                  # iterates through the node next till the end
            if current.key == key:      # node with key found
                if prev:
                    prev.next = current.next  # Removes node by linking previous to next
                else:                   # if node with key not found, keeps iterating
                    self.table[index] = current.next  # Updates head if first node is deleted
                return True  # Key is successfully deleted
            prev = current
            current = current.next

        return False  # Key not found after iterating through the linked list, so it returns false

    # Searches for a key in the hash table
    def search(self, key: int) -> bool:
        index = self.hash_function(key) # getting the index of the key using hashfunction
        current = self.table[index]     # getting the node of the key
        while current:                  # iterate through the node next till the end
            if current.key == key:      # node with key found
                return True             # return True
            current = current.next      # node with key not found, keep iterating
        return False                    # Key not found, return false

    # displaying the hash table
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"{current.key} -> ", end="")
                current = current.next
            print("None")

# Example usage
hash_table = HashTable(10)
hash_table.insert(10)
hash_table.insert(15)
hash_table.insert(20)
hash_table.insert(12)
hash_table.insert(14)
hash_table.insert(25)
hash_table.insert(16)
hash_table.insert(17)
hash_table.insert(18)
hash_table.insert(19)
hash_table.insert(13)
hash_table.insert(21)
hash_table.insert(31)
hash_table.insert(34)
hash_table.insert(26)
print("11 Key found:", hash_table.search(11))
print("26 Key found:", hash_table.search(26))

print("Before deletion:")
hash_table.display()

print("\nDelete key 15:", hash_table.delete(25))

print("After deletion:")
hash_table.display()
