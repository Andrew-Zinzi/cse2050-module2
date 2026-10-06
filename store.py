class Store:
    """Represents the marketplace managing products and customers"""

    def __init__(self):
        """constructor for Store class"""
        self.products = []
        self.customers = []
    
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