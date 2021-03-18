import os
import sys
sys.path.append(os.path.abspath("./Product.py"))

from Product import *

class Cart:

    products = [Product('Test1', 25.0, 3), Product('Test2', 45.99, 2), Product('Test3', 12.31, 10)]
    
    def __init__(self):
        self.index = len(self.products)
    
    def __str__(self):
        return f'{self.products}'
    
    def __len__(self):
        totalLen = 0
        for product in self.products:
            totalLen += product.quantity
        return totalLen
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.products[self.index]
    
    def add(self, name):
        for product in self.products:
            if(name == product.name):
                product.quantity += 1
                
    def remove(self, name):           
        for product in self.products:
            if(name == product.name):
                product.quantity -= 1
                
    def totalPrice(self):
        total = 0
        for product in self.products:
            total += (product.price * product.quantity)
        return total