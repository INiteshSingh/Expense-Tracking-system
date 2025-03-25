'''This file is to create a class based approach for writing data into the record'''

'''Functions for validation'''
def validate_name(name):
    for i in name:
        if i in list("-!@#$%^&*()"):
            print("Name is Invalid Try Again :")

'''class for items objects'''
class items:
    def get_items(self):
        while True:
            try:
                self.name = str(input("Enter Your Item Name: "))
                validate_name(self.name)
                self.itemQuantity = int(input("Enter Item Quantity: "))

            except ValueError:
                print("Entred Invalid Number for Item Quantity Try again!")

                self.itemPrice = int(input("Enter Price of a single Item: "))
            except ValueError:
                print("Enterd Invalid Number for Item Price Try again!")

                self.itemTotal = self.itemQuantity * self.itemPrice

                print("\nThis is the data you entered: ")
                print("\tItem Name: ",self.name)
                print("\tItem Quantity: ",self.itemQuantity)
                print("\tItem Price per Unit: ",self.itemPrice)
                print("\tItem Total: ",self.itemTotal)
            
            
                break

a = items()
a.get_items()   
'''For Now the exception is working only for a single wrong input try and fix that'''