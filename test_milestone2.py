import unittest
from order import Order
from customer import Customer
from product import Product
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from store import Store
from cart import ShoppingCart


class TestOrder(unittest.TestCase):
    """Test suite for Order class functionality."""

    def test_order_creation_and_status(self):
        """Test initial order creation and updating status behavior."""
        customer = Customer("C100", "Alex")
        product = Product("P100", "Wireless Mouse", 29.99)
        
        order1 = Order("01", customer, [product])
        self.assertEqual(order1.get_status(), "PENDING")
        
        order1.set_status("PROCESSING")
        self.assertEqual(order1.get_status(), "PROCESSING")
        
    def test_cart_independence_and_total(self):
        """Test total calculation and order item stability after creation."""
        customer = Customer("C100", "James")
        product = Product("P100", "Wireless Mouse", 29.99)
        
        order1 = Order("01", customer, [product])
        self.assertEqual(order1.calculate_total(), 29.99)


class TestLinkedList(unittest.TestCase):
    """Test suite for LinkedList public behavior and operations."""

    def test_add_first(self):
        """Test adding items to the front of the linked list."""
        LL = LinkedList()
        LL.add_first(3)
        self.assertEqual(LL.get_first(), 3)
        
    def test_add_last(self):
        """Test appending items to the end of the linked list."""
        LL = LinkedList()
        LL.add_first(3)
        LL.add_last(2)
        self.assertEqual(LL.get_first(), 3)
        self.assertEqual(LL.size(), 2)
        
    def test_remove_first(self):
        """Test removing the head element and verifying size reduction."""
        LL = LinkedList()
        LL.add_first(3)
        LL.add_last(2)
        self.assertEqual(LL.remove_first(), 3)
        self.assertEqual(LL.get_first(), 2)
        self.assertEqual(LL.size(), 1)
        
    def test_edge_cases(self):
        """Test operations on an empty linked list."""
        LL = LinkedList()
        self.assertEqual(LL.remove_first(), None)
        self.assertEqual(LL.get_first(), None)
        self.assertEqual(LL.size(), 0)
        self.assertEqual(LL.is_empty(), True)


class TestStack(unittest.TestCase):
    """Test suite for Stack LIFO behavior."""

    def test_lifo_order(self):
        """Test that elements pop in last-in, first-out order."""
        stack1 = Stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        
        self.assertEqual(stack1.pop(), 3)
        self.assertEqual(stack1.pop(), 2)
        self.assertEqual(stack1.pop(), 1)
        
    def test_peek(self):
        """Test looking at top item without removing it."""
        stack1 = Stack()
        stack1.push(1)
        stack1.push(2)
        stack1.push(3)
        
        self.assertEqual(stack1.peek(), 3)
        stack1.pop()
        self.assertEqual(stack1.peek(), 2)
        
    def test_pop_empty_stack(self):
        """Test popping from an empty stack returns None."""
        stack1 = Stack()
        self.assertIsNone(stack1.pop())


class TestQueue(unittest.TestCase):
    """Test suite for OrderQueue FIFO behavior."""

    def test_fifo_order(self):
        """Test that elements dequeue in first-in, first-out order."""
        OQ = OrderQueue()
        OQ.enqueue(1)
        OQ.enqueue(2)
        OQ.enqueue(3)
        
        self.assertEqual(OQ.dequeue(), 1)
        self.assertEqual(OQ.dequeue(), 2)
        self.assertEqual(OQ.dequeue(), 3)
        
    def test_peek(self):
        """Test looking at front item without dequeuing it."""
        OQ = OrderQueue()
        OQ.enqueue(1)
        OQ.enqueue(2)
        OQ.enqueue(3)
        
        self.assertEqual(OQ.peek(), 1)
        OQ.dequeue()
        self.assertEqual(OQ.peek(), 2)
        
    def test_dequeue_empty_stack(self):
        """Test dequeuing from an empty queue returns None."""
        OQ = OrderQueue()
        self.assertIsNone(OQ.dequeue())


class TestStoreIntegration(unittest.TestCase):
    """Test suite for store checkout, order processing, and history."""

    def test_checkout(self):
        """Test customer checkout creating pending orders and clearing cart."""
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
        """Test dequeuing waiting orders and updating status to processing."""
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
        """Test retrieving processed order history in reverse chronological order."""
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