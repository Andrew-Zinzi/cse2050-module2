from customer import Customer
from product import Product

class Order:
    def __init__(self, order_id: str, customer: Customer, items: list[Product]):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = "PENDING"
        
    def get_id(self):
        return self.order_id
    
    def get_customer(self):
        return self.customer
    
    def get_items(self):
        return self.items
    
    def get_status(self):
        return self.status
    
    def set_status(self, status: str):
        self.status = status
        
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.get_price
        
        return total