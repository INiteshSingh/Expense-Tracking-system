import os
import my_classes as c
#This Module is for storing all the functions for the Expense Tracking System 

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
    print("1.Create a New Record")
    print("2.Add New Records")
    print("3.View Current Records")
    print("4.Delete a Record")
    print("5.Get The Record in Whatsapp Message")


'''This Function When Called Creates a New Folder on the desktop named "Records" and all the records are present 
    in that folder'''
def createRecord():
    try:
        File_path = "C:\\Users\\nt984\\Desktop\\Expense-Tracking-System\\Records" #Creates a Folder Named Reocrds
        if os.path.exists(File_path):
            print("The File Already Exists Write The Data in it")
        elif not os.path.exists(File_path):
            os.makedirs(File_path)
            print("Folder Created Successuflly at the following location {}".format(str(File_path)))
        with open( "C:\\Users\\nt984\\Desktop\\Expense-Tracking-System\\Records\\record1.txt",'w') as f: #Creates a new file Named record.txt to store the records in the records folder.
            data = "Python Expense Tracking System For Traking My Expenses\n"
            f.write(data)
    except FileExistsError:
        print("File Alreay Exits")
    except :
        print("Some Error Occured try again :/")


'''The Following Function is to add a new record in the file, The item.'''
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
