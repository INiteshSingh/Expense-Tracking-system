#This is the main file for creating a expense tracking system where the main purpose is to Tracking all my Purchases for 
#Shop and save them in either a database or a text file

#This first Prototype is using the file system in files 
import my_module as mm

while True:
    # try:
        mm.menu()
        print("*"*20)
        choice = int(input("Enter Your Choice From the Above: "))
        print("*"*20)
        if choice == 1:
            mm.createRecord() #This is not working see tommorow (20 march 2025)
            break
        elif choice == 2:
            mm.viewRecords()
            break
        elif choice == 3:
            mm.addNewRecord()
            break
        elif choice == 4:
            mm.delteRecords()
            break
        else:
            print("The Choice you Enterd is wrong Try again!")
            break
    # except:
    #     print("Some Error Occured Check the Code and try again!")
