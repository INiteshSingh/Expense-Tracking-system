#The Main File is For all the function calls 
import my_module as m
while True:
    try:
        m.menu()
        print("*"*70)
        choice = int(input("Enter Your Choice From The Above :"))
        print("*"*70)
        
        if choice == 1:
            m.createRecord()
            break
        elif choice == 2:
            m.addNewRecord()
            break
        elif choice == 3:
            m.viewRecords()
            break
        elif choice == 4:
            m.delteRecords()
            break
        elif choice == 5:
            print("The Whatsapp Functionality is still Under Development")
            break   # For Future Function, here add the function to get the record to whatsapp
        else:
            print("Enter Only The Values From 1-5") 
    except ValueError:
        print("Enter Only Numerical Values for choice not anything else")
    except :
        print("Something Went Wrong Check the code")