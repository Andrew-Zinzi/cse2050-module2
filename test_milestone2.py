import unittest
from order import Order
from customer import Customer
from product import Product
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderedQueue

class TestOrder(unittest.TestCase):
    def test_order_creation_and_status(self):
        customer = Customer("C100", "Alex")
        product = Product("P100", "Wireless Mouse", 29.99)
        
        order1 = Order("01", customer, [product])
        
        self.assertEqual(order1.get_status(), "PENDING")
        
        order1.set_status("PROCESSING")
        self.assertEqual(order1.get_status(), "PROCESSING")
        
    # def test_cart_independence_and_total(self):
    #     order

class TestLinkedList(unittest.TestCase):
    def test_add_first(self):
        LL = LinkedList()
        LL.add_first(3)
        self.assertEqual(LL.get_first(), 3)
        
    def test_add_last(self):
        LL = LinkedList()
        LL.add_first(3)
        LL.add_last(2)
        self.assertEqual(LL.get_first(), 3)
        self.assertEqual(LL.size(), 2)
        
    def test_remove_first(self):
        LL = LinkedList()
        LL.add_first(3)
        LL.add_last(2)
        self.assertEqual(LL.remove_first(), 3)
        self.assertEqual(LL.get_first(), 2)
        self.assertEqual(LL.size(), 1)
        
    def test_edge_cases(self):
        LL = LinkedList()
        self.assertEqual(LL.remove_first(), None)
        self.assertEqual(LL.get_first(), None)
        self.assertEqual(LL.size(), 0)
        self.assertEqual(LL.is_empty(), True)
        
class TestStack(unittest.TestCase):
    def test_lifo_order(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        
        self.assertEqual(stack1.pop(), 3)
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        
    def test_peek(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        
        self.assertEqual(stack1.peek(), 3)
        
        stack1.pop()
        
        self.assertEqual(stack1.peek(), 2)
        
    def test_pop_empty_stack(self):
        stack1 = Stack()
        self.assertIsNone(stack1.pop())
        
class TestQueue(unittest.TestCase):
    def test_fifo_order(self):
        OQ = OrderedQueue()
        OQ.enqueue(1)
        OQ.enqueue(2)
        OQ.enqueue(3)
        
        self.assertEqual(OQ.dequeue(), 1)
        self.assertEqual(OQ.dequeue(), 2)
        self.assertEqual(OQ.dequeue(), 3)
        
    def test_peek(self):
        OQ = OrderedQueue()
        OQ.enqueue(1)
        OQ.enqueue(2)
        OQ.enqueue(3)
        
        self.assertEqual(OQ.peek(), 1)
        
        OQ.dequeue()
        
        self.assertEqual(OQ.peek(), 2)
        
    def test_dequeue_empty_stack(self):
        OQ = OrderedQueue()
        self.assertIsNone(OQ.dequeue())
        
        
if __name__ == '__main__':
    unittest.main()