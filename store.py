from order_queue import OrderQueue
from stack import Stack
from order import Order

class Store:
    """Represents the marketplace managing products, customers, and orders."""

    def __init__(self):
        """Initialize empty product, customer, order records, queue, and stack."""
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderQueue()
        self.order_history = Stack()
        self.order_counter = 0
    
    def add_product(self, product) -> bool:
        """Add a product to the store if its ID is unique."""
        if self.find_product(product.get_id()) is not None:
            return False
        self.products.append(product)
        return True
    
    def find_product(self, product_id: str):
        """Find and return a Product by ID, or None if not found."""
        for item in self.products:
            if item.get_id() == product_id: 
                return item
        return None
    
    def add_customer(self, customer) -> bool:
        """Add a customer to the store if its ID is unique."""
        if self.find_customer(customer.get_id()) is not None:
            return False
        self.customers.append(customer)
        return True
            
    def find_customer(self, customer_id: str):
        """Find and return a Customer by ID, or None if not found."""
        for item in self.customers:
            if item.get_id() == customer_id:
                return item
        return None
    
    def find_order(self, order_id: str):
        """Find and return an Order by ID, or None if not found."""
        for item in self.orders:
            if item.get_id() == order_id:
                return item
        return None
            
    def get_orders(self):
        """Return the permanent list of all store orders."""
        return self.orders
    
    def checkout(self, customer_id: str):
        """Create an order from a customer's cart, queue it, and clear the cart."""
        customer = self.find_customer(customer_id)
        if customer is None or customer.get_cart().is_empty():
            return None
        
        self.order_counter += 1
        order_id = f"O{self.order_counter}"
        cart_items = list(customer.get_cart().get_items())                

        new_order = Order(order_id, customer, cart_items)

        self.orders.append(new_order)
        self.order_queue.enqueue(new_order)
        customer.get_cart().clear()
        
        return new_order
    
    def process_next_order(self):
        """Dequeue the oldest order, set status to PROCESSING, and push to history."""
        if self.order_queue.is_empty():
            return None
        
        current_order = self.order_queue.dequeue()
        current_order.set_status("PROCESSING")
        self.order_history.push(current_order)
        return current_order
    
    def get_order_history(self):
        """Return a list of processed orders from most recent to oldest."""
        history_list = []
        temp_stack = Stack()
        
        while not self.order_history.is_empty():
            order = self.order_history.pop()
            history_list.append(order)
            temp_stack.push(order)
            
        while not temp_stack.is_empty():
            self.order_history.push(temp_stack.pop())
            
        return history_list