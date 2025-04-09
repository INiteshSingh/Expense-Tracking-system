import numpy as np
import mysql.connector
'''This file is to create a class based approach for writing data into the record'''

'''Functions for validation'''
def validate_name(name):
    for i in name:
        if i in list("-!@#$%^&*()"):
            print("Name is Invalid Try Again :")

'''class for items objects'''
class item:
    def getInfo(self): #For Adding the data when purchasing new items
        self.itemName = str(input("Enter Item Name: "))
        self.itemQuantity = int(input("Enter Item Quantity: "))
        self.itemPrice = float(input("Enter The Price of a single Unit: "))
        self.itemTotal = self.itemQuantity * self.itemPrice

        print("Enterd Data: ")
        for k,v in self.__dict__.items():
            print(k," ---> ",v)
    #mysql://root:mfcfnwwTVmVbvRbzOZlfeIIWrLEhSwrk@maglev.proxy.rlwy.net:21724/railway
    def writeData(self):
        db_config = {
            "host": "maglev.proxy.rlwy.net",  # Replace with actual IP or localhost if needed
            "user": "root",
            "password": "mfcfnwwTVmVbvRbzOZlfeIIWrLEhSwrk",  # Replace with your password
            "database": "railway",  # Ensure this is the correct database name
            "port": 21724  # Ensure this is an integer
        }

        print(f"Connecting with config: {db_config}")  # Debugging connection parameters

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            print("✅ Successfully connected to Railway MySQL!")
            
            sql = "INSERT INTO Store_items_list (Item_name, Item_quantity, Item_price) VALUES (%s, %s, %s);"
            values = (self.itemName, self.itemQuantity, self.itemPrice)
            cursor.execute(sql, values)
            conn.commit()
            print(f"Inserted {values}")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print(f"Some Error Occurred: {err}")
        
a = item()
a.getInfo()
a.writeData()

