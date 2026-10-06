class Product:
    """Represents a product available for purchase in the store."""

    def __init__(self, product_id: str, name: str, price: float):
        """Initialize a product with an ID, name, and price."""
        self.product = product_id
        self.names = name
        self.prices = price

    def get_id(self):
        """Return the unique product ID."""
        return self.product

    def get_name(self):
        """Return the name of the product."""
        return self.names

    def get_price(self):
        """Return the price of the product."""
        return self.prices