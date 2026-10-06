class Product:
    def __init__(self, product_id: str, name: str, price: float):
        self.product = product_id
        self.names = name
        self.prices = price

    def get_id(self):
        return self.product

    def get_name(self):
        return self.names

    def get_price(self):
        return self.prices
    