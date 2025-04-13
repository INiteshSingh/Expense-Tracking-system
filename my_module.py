import os
import mysql.connector 
from mysql.connector import Error
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


def connect_and_operate(host, user, password, database=None, sql=None):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        
        if sql:
            cursor.execute(sql)
            if sql.strip().lower().startswith(("select", "show")):
                result = cursor.fetchall()
                for row in result:
                    print(row)
        
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Operation completed successfully.")
    except Error as e:
        print(f"❌ Error: {e}")

'''Performs an sql operation on the local data base the parameter -sql- is the actual sql query '''
def perform_sql_operation(sql):
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "nitesh@1357",
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
         

def create_new_db():
    print("You are Attempting to Create a New Database")
    choice = str(input("Do You Want to create a New Database (y/n): "))
    if choice.lower() == "y":
        print("Enter Desired Name for your Data Base: ")
        global db_name 
        db_name = str(input("Enter a Name For Your Database: "))
        connect_and_operate("localhost","root","nitesh@1357",sql=f"CREATE DATABASE IF NOT EXISTS {db_name};")
        print("Creating a New Database 🗂️")
        print("Created Database Successfully ✅")
    else:
        print("Database Creation Cancelled ❌")

def create_new_table():
    try:
        print("You are Attempting to Create a New Table")
        choice = str(input("Do You Want to create a New Table (y/n): "))
        if choice.lower() == "y":
            table_name = str(input("Enter Table Name To Create: "))
            if table_name == " ":
                print("Enter Correct Value for Table Name: ")
            else:
                sql = f"CREATE TABLE {table_name} ;"
                connect_and_operate("localhost","root","nitesh@1357","purchase_records",sql)
                print("Creating New Table 🗂️")
                print("New Table Created Successfully ✅")
        else:
            print("Table Creation Cancelled ❌")
    except ValueError:
        print("Enter Correct Choice")
