from datetime import date
import customtkinter as ctk

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
    def __init__(self, userID, name, email, password, phoneNumber, balance):
        self.__userID = userID   
        self.__name = name  
        self.__email = email   
        self.__password = password  
        self.__phoneNumber = phoneNumber   
        self.__transactionList = [] 
        self.__balance = balance
        self.__userID = userID

    def deposit(self, inDeposit):
        self.__balance += inDeposit

    def purchase(self, inTransaction):
        itemsPrice = inTransaction.price * inTransaction.quantity

        if (self.__balance > itemsPrice):
            self.__balance -= itemsPrice
            self.__transactionList.append(inTransaction)
        else:
            pass

    def getDetails(self):
        list = (self.__userID, self.__name, self.__email, self.__password, self.__phoneNumber, self.__balance)
        return list
    
    def getTransactions(self):
        return self.__transactionList
    

class Inventory:
    pass


