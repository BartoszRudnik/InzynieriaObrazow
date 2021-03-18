class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity        
    
    def __str__(self):
        return f'Product name is {self.name} and price is {self.price}'
    
    def __repr__(self):
        return f'Product name is {self.name}, price is {self.price} and quantity is {self.quantity}'