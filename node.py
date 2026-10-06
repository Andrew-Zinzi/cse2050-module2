class Node:
    """Stores a single data element and a reference to the next node."""
    
    def __init__(self, data, next=None):
        """Initialize a node with data and optional reference to the next node."""
        self.data = data
        self.next = next
        