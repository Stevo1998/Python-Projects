from abc import ABC, abstractmethod # Importing the abstractmethod from the abc module

class Bills(ABC): # Parent class
    def utilities(self, total):
        print:("Total amount due for utilities:  ",total) # Passing in the argument "total" to he function

    def insurance(self, total):
        print:("Total amount due for insurance: ",total)

    @abstractmethod # Defying the abstract method
    def payment(self, total):
        pass

class DebitCard(Bills): # Child class
    def payment(self, total):# Using the abstract method passed from the parent class
        print('Your total amount of {} for utilities has been charged on your debit card. '.format(total))

class CreditCard(Bills):
    def payment(self, total): # Using the abstract method passed from the parent class
        print('Your total amount of {} for insurance has been charged on your credit card. '.format(total))

#Printing the defined method for tthe classes
objD = DebitCard()
objD.utilities("$250")
objD.payment("$250")
objC = CreditCard()
objC.insurance("$188")
objC.payment("$188")

