from customer import Customer
from product import Product

class Order:
    """Represents a customer's order snapshot and processing status."""

    def __init__(self, order_id: str, customer: Customer, items: list[Product]):
        """Initialize an order with an ID, customer, items, and pending status."""
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = "PENDING"
        
    def get_id(self):
        """Return the order ID."""
        return self.order_id
    
    def get_customer(self):
        """Return the customer who placed the order."""
        return self.customer
    
    def get_items(self):
        """Return the list of products in the order."""
        return self.items
    
    def get_status(self):
        """Return the current processing status of the order."""
        return self.status
    
    def set_status(self, status: str):
        """Update the order processing status."""
        self.status = status
        
    def calculate_total(self):
        """Return the total price of all items in the order."""
        total = 0
        for item in self.items:
            total += item.get_price()
        return total