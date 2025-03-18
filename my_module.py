#This Module is for storing all the functions for the Expense Tracking System 

def createRecord():
    with open('record.txt','w') as f:
        data = "Python Expense Tracking System For Traking My Expenses"
        f.write(data)

def addNewRecord(info):
    with open('record.txt','a') as f:
        data = info
        f.write(data)

def viewRecords():
    with open('record.txt','r') as f:
        print(f.read())