from linked_list import LinkedList

class OrderedQueue:
    def __init__(self):
        self._list = LinkedList()
    
    def enqueue(self, item):
        self._list.add_last(item)
    
    def dequeue(self):
        if self._list.is_empty():
            return None
                
        return self._list.remove_first()
    
    def peek(self):
        return self._list.get_first()
    
    def is_empty(self):
        return self._list.is_empty()
    
    def size(self):
        return self._list.size()