from node import Node

class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0
        
    def add_first(self, item):
        node = Node(item)
        if self._len == 0:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._len += 1
        
    def add_last(self, item):
        node = Node(item)
        if self._len == 0:
            self.add_first(item)
        else:
            self._tail.next = node
            self._tail = node
            
        self._len += 1
            
    def remove_first(self):
        if self._len == 0: return None
        
        removed_node = self._head
        self._head = self._head.next
        self._len -= 1
        
        return removed_node.data
    
    def get_first(self):
        if self._len == 0: return None
        
        return self._head.data
    
    def is_empty(self):
        return self._len == 0
    
    def size(self):
        return self._len