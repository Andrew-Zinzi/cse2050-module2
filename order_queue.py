from linked_list import LinkedList

class OrderQueue:
    """FIFO data structure implemented as a wrapper around LinkedList."""

    def __init__(self):
        """Initialize an empty queue backed by a LinkedList."""
        self._list = LinkedList()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._list.add_last(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue, or None if empty."""
        if self._list.is_empty():
            return None
        return self._list.remove_first()
    
    def peek(self):
        """Return the front item from the queue without removing it."""
        return self._list.get_first()
    
    def is_empty(self):
        """Return True if the queue contains no items."""
        return self._list.is_empty()
    
    def size(self):
        """Return the number of items in the queue."""
        return self._list.size()