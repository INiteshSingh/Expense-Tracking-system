#This is the main file for creating a expense tracking system where the main purpose is to Tracking all my Purchases for 
#Shop and save them in either a database or a text file

#This first Prototype is using the file system in files 
import my_module as mm


while True:
        try:
            choice = str(input("Do You Want to create a new Record (y/n)"))
            break
        except ValueError:
             print("Enter Only y or n")
if choice.lower()=="y":
    mm.createRecord()
else:
    print("Thank You For Using this Program! ")
