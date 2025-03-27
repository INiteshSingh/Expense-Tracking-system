'''This file is to create a class based approach for writing data into the record'''

'''Functions for validation'''
def validate_name(name):
    for i in name:
        if i in list("-!@#$%^&*()"):
            print("Name is Invalid Try Again :")

'''class for items objects'''
class item:
    def getInfo(self): 
        self.itemName = str(input("Enter Item Name: "))
        self.itemQuantity = int(input("Enter Item Quantity: "))
        self.itemPrice = float(input("Enter The Price of a single Unit: "))
        self.itemTotal = self.itemQuantity * self.itemPrice

        print("Enterd Data: ")
        for k,v in self.__dict__.items():
            print(k," ---> ",v)

    def writeData(self):
        items_dict = {"Item Name => " : self.itemName,
                      "Item Quantity => " : self.itemQuantity,
                      "Item Price => " : self.itemPrice,
                      "Item Total => " : self.itemTotal}
        
        print("Data Trying To Enter {}".format(items_dict))
        choice = str(input("SAVE DATA ? (Y/N): "))
        if choice != "y":
            print("Thank You For Using This Program")
        else:
            with open('C:\\Users\\nt984\\Desktop\\Expense-Tracking-system\\Records\\record1.txt','a') as f:
                data = str(items_dict)
                f.write("\n")
                f.write(data)
                f.write("\n")
            print("Data Saved Successfully")
                
                
