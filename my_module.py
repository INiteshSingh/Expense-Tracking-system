#This Module is for storing all the functions for the Expense Tracking System 
def menu():
    print("1.Create a New Record")
    print("2.View Current Records")
    print("3.Add New Records")
    print("4.Delete a Record")
    print("5.Get The Record in Whatsapp Message")

def createRecord():
    with open('record.txt','w') as f:
        data = "Python Expense Tracking System For Traking My Expenses"
        f.write(data)

'''The Following Function is to add a new record in the file, The parameter info is just string data that 
   contains what did i buy in a specific time.'''
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
