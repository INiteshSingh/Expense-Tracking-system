import os
#This Module is for storing all the functions for the Expense Tracking System 
def menu():
    print("1.Create a New Record")
    print("2.View Current Records")
    print("3.Add New Records")
    print("4.Delete a Record")
    print("5.Get The Record in Whatsapp Message")

'''This Function When Called Creates a New Folder on the desktop named "Records" and all the records are present 
    in that folder'''
def createRecord():
    try:
        path = "C:\\Users\\nt984858\\Desktop\\Records" #Path to the folder, edit it when using the program in your computer based on your own pc
        if not os.path.exists(path):
            os.makedirs(path)
            print("Created a New Folder at {} Check if You Want.".format(str(path)))
        with open('C:\\Users\\nt984858\\Desktop\\Records\\record.txt','w') as f: #Creates a new file Named record.txt to store the records in the records folder.
            data = "Python Expense Tracking System For Traking My Expenses"
            f.write(data)
    except FileExistsError:
        print("File Alreay Exits")
    except :
        print("Some Error Occured try again :/")

'''The Following Function is to add a new record in the file, The parameter info is just storing data that 
   contains what did i buy at a specific time.'''
def addNewRecord(info):
    while True:
        try:
            with open('record.txt','a') as f:
                data = info
                f.write(data)
                break
        except FileNotFoundError:
            print("The Specified file does not exists")
            print("Enter Valid File Name")

'''The Following Function is used to view all the current records, All the records are always in a single line.'''
def viewRecords():
    while True:
        try:
            with open('record.txt','r') as f:
                print(f.read())
                break
        except FileNotFoundError:
            print("The Specified file does not exists, Check the code for any errors or bugs")
            
'''The Following Function is for deleting all the current records of present in the folder'''
def delteRecords():
    try:
        with open('recod.txt','w') as f:
            f.write(" ")
    except FileNotFoundError:
            print("The Specified File does not exists check for code")
