import unittest
from order import Order
from customer import Customer
from product import Product
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderedQueue
from store import Store
from cart import ShoppingCart

class TestOrder(unittest.TestCase):
    def test_order_creation_and_status(self):
        customer = Customer("C100", "Alex")
        product = Product("P100", "Wireless Mouse", 29.99)
        
        order1 = Order("01", customer, [product])
        
        self.assertEqual(order1.get_status(), "PENDING")
        
        order1.set_status("PROCESSING")
        self.assertEqual(order1.get_status(), "PROCESSING")
        
    def test_cart_independence_and_total(self):
        customer = Customer("C100", "James")
        product = Product("P100", "Wireless Mouse", 29.99)
        
        order1 = Order("01", customer, [product])
        self.assertEqual(order1.calculate_total(), 29.99)

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

class TestStoreIntegration(unittest.TestCase):
    def test_checkout(self):
        store = Store()
        
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)   
        
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)

        john = Customer("C100", "John")
        
        store.add_customer(john)
        
        john_cart = john.get_cart()
        john_cart.add_product(keyboard)
        john_cart.add_product(headphones)
        john_order = store.checkout("C100")
        
        self.assertEqual(john_order.get_id(), "01")
        self.assertEqual(john_order.get_customer().get_name(), "John")
        self.assertEqual(john_order.calculate_total(), 99.98)
        self.assertEqual(john_order.get_status(), "PENDING")
        self.assertEqual(john_cart.is_empty(), True)
        
    def test_processing(self):
        store = Store()
                
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)   
                
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)
        
        john = Customer("C100", "John")
                
        store.add_customer(john)
                
        john_cart = john.get_cart()
        john_cart.add_product(keyboard)
        john_cart.add_product(headphones)
        john_order = store.checkout("C100")
                
        first_order = store.process_next_order()
        self.assertEqual(first_order.get_id(), "01")
        self.assertEqual(first_order.get_status(), "PROCESSING")
        self.assertIsNone(store.process_next_order())
        
    def test_history(self):
        store = Store()
                
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)   
                
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)
        
        john = Customer("C100", "John")
                
        store.add_customer(john)
                
        john_cart = john.get_cart()
        john_cart.add_product(keyboard)
        john_cart.add_product(headphones)
        john_order = store.checkout("C100")
        
        bob = Customer("C101", "Bob")
                
        store.add_customer(bob)
                
        bob_cart = bob.get_cart()
        bob_cart.add_product(keyboard)
        bob_cart.add_product(headphones)
        bob_order = store.checkout("C101")
        
        first_order = store.process_next_order()
        second_order = store.process_next_order()
        
        history = store.get_order_history()
        self.assertEqual(history[0].get_id(), "02")
        self.assertEqual(history[1].get_id(), "01")

if __name__ == '__main__':
    unittest.main()