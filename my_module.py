import os
import mysql.connector 
import myClass as c
#This Module is for storing all the functions for the Expense Tracking System 

"""Prints a Banner with some Art on the terminal"""
def banner():   
    print(r"""  _______  ______  _____ _   _ ____  _____   
 | ____\ \/ /  _ \| ____| \ | / ___|| ____|  
 |  _|  \  /| |_) |  _| |  \| \___ \|  _|    
 | |___ /  \|  __/| |___| |\  |___) | |___   
 |_____/_/\_\_|   |_____|_| \_|____/|_____|  
 |_   _|  _ \    / \  / ___| |/ / ____|  _ \ 
   | | | |_) |  / _ \| |   | ' /|  _| | |_) |
   | | |  _ <  / ___ \ |___| . \| |___|  _ < 
   |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\
                                             """)
def menu():
    print("1.Create a New Data Base")
    print("2.Create a New Table")
    print("3.Add New Records")
    print("4.View Current Records")
    print("5.Delete a Record")
    print("6.Perform an sql data base operation")


'''Performs an sql operation on the local data base the parameter -sql- is the actual sql query '''
def perform_sql_operation(sql):
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "nitesh@1357"
        )

        cursor = conn.cursor()
        
        cursor.execute(sql)

        print("Exectuing Your SQL Query ⏳")
        print("Executed Your Query successfully ✅")

         # If it's a SELECT/SHOW query, fetch results
        if sql.strip().lower().startswith(("select", "show")):
            results = cursor.fetchall()
            for row in results:
                print(row)  # Optional: show results to user

        cursor.close()
        conn.close()
    except Exception as e:
         print(f"⚠️ Warning Some Error Occured: \n \t{e}")
         
"""Creting a new Data base locally"""
def createDatabase():
    try:
        print("You Are Attempting to Create a New Data Base 📦")
        agree = str(input("Do You Want to Create a new Data Base ? (y/n): "))
        if agree.lower() ==  "y":
            print(f"Got input {agree}, Creating A New DataBase 🔄")
            db_name = str(input("Enter Your Desired Data Base Name: "))
            sql = f"CREATE DATABASE {db_name}"
            perform_sql_operation(sql)
        else:
             print("Data Base Creation Cancelled ❌")

    except ValueError:
        print("Error Occured ❌, Enter Valid Input: ")
    except Exception as e:
         print("Warning Some Error Occured ⚠️: \n {e}")
    return sql


def create_table_in_db():
    perform_sql_operation("SHOW DATABASES;")
    db_name = str(input("select and enter the database where you want to create a table: "))

    print(f"Creating a table in the Data base {db_name}")
    print("The Defalut Columns are Serial Number : s_no, Item Name: item_name, Item Quantity: item_quantity, Total Price: tot_price: ")
    agree = str(input("Do You Want To Create the Table with the following stroge options: (y/n)"))

    if agree.lower() == "y":
        table_name = str(input("Enter Table Name to add in the Data Base: "))
        sql = f"CREATE TABLE {table_name} (s_no INT AUTO_INCREMENT PRIMARY KEY, item_name VARCHAR(50) NOT NULL,item_quantity INT NOT NULL, total_price DECIMAL(10,2) NOT NULL, price_per_unit DECIMAL(10,2) GENERATED ALWAYS AS (total_price/item_quantity) STORED);"
        perform_sql_operation(sql)
    else:
         print("Thank You For Using the app :) ")

'''The Following Function is to add a new record in the local database, The values are s.no, item_name, 
    item_quantity, item_price, bought_on.'''
def addNewRecord():
        try:
            s = c.item()
            s.getInfo()
            s.writeData()
        except :
             print("Something Went Wrong Try again !")
        

'''The Following Function is used to view all the current records, All the records are always in a single line.'''
def viewRecords():
        try:
            with open('C:\\Users\\nt984\\Desktop\\Expense-Tracking-system\\Records\\record1.txt','r') as f:
                print(f.read())
        except FileNotFoundError:
            print("The Specified file does not exists, Check the code for any errors or bugs")
            
'''The Following Function is for deleting all the current records of present in the folder'''
def delteRecords():
    try:
        with open('recod.txt','w') as f:
            f.write(" ")
    except FileNotFoundError:
            print("The Specified File does not exists check for code")

'''Validations of Input for all the inputs in the Program'''

def validate_choice(choice):
    right_options = list(val for val in range(1,6))
    if choice not in right_options:
        print("Enter Only the Following Values: {}".format(right_options))

def validate_choice1(choice):
    right_options = ["y","n"] 
    if choice not in right_options:
        print("Enter Options only From {}".format(right_options))
