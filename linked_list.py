from node import Node

class LinkedList:
    """Singly linked list implementation maintaining head and tail references."""

    def __init__(self):
        """Initialize an empty linked list."""
        self._head = None
        self._tail = None
        self._len = 0
        
    def add_first(self, item):
        """Add an item to the front of the linked list."""
        node = Node(item)
        if self._len == 0:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._len += 1
        
    def add_last(self, item):
        """Add an item to the end of the linked list."""
        node = Node(item)
        if self._len == 0:
            self.add_first(item)
        else:
            self._tail.next = node
            self._tail = node
            self._len += 1
            
    def remove_first(self):
        """Remove and return the first item in the list, or None if empty."""
        if self._head is None: 
            return None
        
        data = self._head.data
        self._head = self._head.next
        self._len -= 1
        
        if self._head is None:
            self._tail = None
        
        return data
    
    def get_first(self):
        """Return the first item in the list without removing it."""
        if self._len == 0:
            return None
        return self._head.data
    
    def is_empty(self):
        """Return True if the linked list contains no items."""
        return self._len == 0
    
    def size(self):
        """Return the number of items in the linked list."""
        return self._len