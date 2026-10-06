from cart import ShoppingCart

class Customer:
    """Represents a store customer with a unique ID and shopping cart."""

    def __init__(self, customer_id: str, name: str):
        """Initialize a customer with an ID, name, and empty shopping cart."""
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()

    def get_id(self):
        """Return the customer ID."""
        return self.customer_id

    def get_name(self):
        """Return the name of the customer."""
        return self.name

    def get_cart(self):
        """Return the customer's shopping cart."""
        return self.cart