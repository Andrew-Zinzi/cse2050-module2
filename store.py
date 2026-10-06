from order_queue import OrderedQueue
from stack import Stack
from order import Order

class Store:
    """Represents the marketplace managing products and customers"""

    def __init__(self):
        """constructor for Store class"""
        self.products = []
        self.customers = []
        self.orders = []
        self.order_queue = OrderedQueue()
        self.order_history = Stack()
        self.order_counter = 0
    
    def add_product(self, product) -> bool:
        """Initializes empty product and customer lists"""
        if self.find_product(product.get_id()) is not None:
            return False
        
        self.products.append(product)
        return True
    
    def find_product(self, product_id: str):
        """Find and return a Product by ID; return None when not found"""
        for item in self.products:
            if item.get_id() == product_id: 
                return item
            
        return None
    
    def add_customer(self, customer) -> bool:
        """Add a customer if its ID is not already stored"""
        if self.find_customer(customer.get_id()) is not None:
            return False
        
        self.customers.append(customer)
        return True
            
        
    def find_customer(self, customer_id: str):
        """Find and return a Customer by ID; return None when not found"""
        for item in self.customers:
            if item.get_id() == customer_id:
                return item
        
        return None
    
    def find_order(self, order_id: str):
        for item in self.orders:
            if item.get_id() == order_id:
                return item
            
        return None
            
    def get_orders(self):
        return self.orders
    
    def checkout(self, customer_id: str):
        customer = self.find_customer(customer_id)
        if customer is None or customer.get_cart().is_empty():
            return None
        
        self.order_counter += 1
        order_id = f"{self.order_counter:02d}"
        cart_items = list(customer.get_cart().get_items())                

        new_order = Order(order_id, customer, cart_items)

        self.orders.append(new_order)
        self.order_queue.enqueue(new_order)
        customer.get_cart().clear()
        
        return new_order
    
    def process_next_order(self):
        if self.order_queue.is_empty():
            return None
        
        current_order = self.order_queue.dequeue()
        
        current_order.set_status("PROCESSING")
        self.order_history.push(current_order)
        return current_order
    
    def get_order_history(self):
        history_list = []
        temp_stack = Stack()
        
        while not self.order_history.is_empty():
            order = self.order_history.pop()
            history_list.append(order)
            temp_stack.push(order)
            
        while not temp_stack.is_empty():
            self.order_history.push(temp_stack.pop())
            
        return history_list
            
        