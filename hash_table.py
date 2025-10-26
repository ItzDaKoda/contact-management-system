
class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The Contact object.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, number): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        # Simple hash function: sum ASCII values and mod by table size
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key: str, number: str) -> None:
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        # If slot is empty, place the new node there
        if self.data[index] is None:
            self.data[index] = new_node
            return

        # Otherwise, traverse linked list for duplicate or append
        current = self.data[index]
        while current:
            # Update number if contact already exists
            if current.key == key:
                current.value.number = number
                return
            # Move to next if exists
            if current.next is None:
                break
            current = current.next

        # Append new node at the end of the chain
        current.next = new_node

    def search(self, key: str):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self) -> None:
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            if self.data[i] is None:
                print("Empty")
            else:
                current = self.data[i]
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()



# Testing the Hash Table

if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    print("\n--- Inserting Contacts ---")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\n--- Searching for John ---")
    contact = table.search("John")
    print("Search result:", contact)

    print("\n--- Testing Collisions ---")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\n--- Updating Rebecca's Number ---")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\n--- Searching for Missing Contact ---")
    print("Search result:", table.search("Chris"))



# Design Memo Reflection (200–300 words)


"""
Design Memo Reflection

A hash table is the ideal data structure for fast lookups because it provides near constant-time (O(1)) access on average. 
By converting a key, such as a contact’s name, into an array index through a hash function, the program can jump directly 
to the location where the data is stored instead of searching through an entire list. This makes hash tables especially 
useful for applications like contact directories, caches, and databases where quick retrieval is essential.

In this implementation, I handled collisions using a technique called separate chaining. Each index in the array holds 
a linked list, and if multiple keys map to the same index, the new entries are added to the list. This ensures that 
no data is lost and that multiple contacts can safely exist even if they share the same hash value. When a duplicate 
contact name is inserted, the program updates the existing phone number rather than creating a new entry, which maintains 
data consistency.

An engineer might choose a hash table over a list when lookups and insertions need to be efficient, or when data grows 
large enough that linear searches become too slow. Compared to trees, hash tables offer simpler logic and typically 
faster average-case performance, although they trade off ordered data storage. In real-world systems, this design 
balances speed and flexibility, making it ideal for managing contacts or other key-value pairs.
"""
