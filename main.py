#This is the main file for creating a expense tracking system where the main purpose is to Tracking all my Purchases for 
#Shop and save them in either a database or a text file

#This first Prototype is using the file system in files 
import my_module as mm

while True:
    try:
        mm.menu()
        choice = int(input("Enter Your Choice From the Above"))
        if choice == 1:
            mm.createRecord()
        elif choice == 2:
            mm.viewRecords()
        elif choice == 3:
            mm.addNewRecord()
        elif choice == 4:
            mm.delteRecords()
        else:
            print("The Choice you Enterd is wrong Try again!")
    except:
        print("Some Error Occured Check the Code and try again!")
