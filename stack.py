from linked_list import LinkedList

class Stack:
    """LIFO data structure implemented as a wrapper around LinkedList."""

    def __init__(self):
        """Initialize an empty stack backed by a LinkedList."""
        self._list = LinkedList()
    
    def push(self, item):
        """Add an item to the top of the stack."""
        self._list.add_first(item)
    
    def pop(self):
        """Remove and return the top item from the stack, or None if empty."""
        if self._list.is_empty():
            return None
        return self._list.remove_first()
    
    def peek(self):
        """Return the top item from the stack without removing it."""
        return self._list.get_first()
    
    def is_empty(self):
        """Return True if the stack contains no items."""
        return self._list.is_empty()
    
    def size(self):
        """Return the number of items in the stack."""
        return self._list.size()