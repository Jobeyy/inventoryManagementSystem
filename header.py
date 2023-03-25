from datetime import date

class Product:
    def __init__(self, name, description, price, productID, supplier, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.productID = productID
        self.supplier = supplier
        self.quantity = quantity
        
    
    def updatePrice(self, inPrice):
        self.price = inPrice

    def updateQuantity(self, inQuantity):
        self.quantity = inQuantity

    def getDetails(self):
        list = {
            "name" : self.name,
            "description" : self.description,
            "price" : self.price,
            "productID" : self.productID,
            "supplier" : self.supplier,
            "quantity" : self.quantity
        }
        return list
    
class Transaction:
    pass
class Supplier:
    pass
class User:
    pass
class Inventory:
    pass
