#The Main File is For all the function calls 
import my_module as m
try:
    while True:
        m.menu()
        print("*"*70)
        choice = int(input("Enter Your Choice From The Above :"))
        m.validate_choice(choice)
        print("*"*70)
        
        if choice == 1:
            m.createRecord()
            choice1 = (input("Do You Want to Do Another Opertaion (y/n)"))
            m.validate_choice1(choice1)
            if choice1.lower() == 'n':
                print("\tThank You For Using this program")
                break
        elif choice == 2:
            m.addNewRecord()
            choice1 = (input("Do You Want to Do Another Opertaion (y/n)"))
            m.validate_choice1(choice1)
            if choice1.lower() == 'n':
                print("\tThank You For Using this program")
                break
        elif choice == 3:
            m.viewRecords()
            choice1 = (input("Do You Want to Do Another Opertaion (y/n)"))
            m.validate_choice1(choice1)
            if choice.lower() == 'n':
                print("\tThank You For Using this program")
                break
        elif choice == 4:
            m.deleteRecords()
            choice1 = (input("Do You Want to Do Another Opertaion (y/n)"))
            m.validate_choice1(choice1)
            if choice1.lower() == 'n':
                print("\tThank You For Using this program")
                break
        elif choice == 5:
            print("The Whatsapp Functionality is still Under Development")
            choice1 = (input("Do You Want to Do Another Opertaion (y/n)"))
            m.validate_choice1(choice1)
            if choice.lower() == 'n':
                print("\tThank You For Using this program")
                break   # For Future Function, here add the function to get the record to whatsapp
        else:
            print("Enter Only The Values From 1-5") 
except ValueError:
    print("Enter Only Numerical Values for choice not anything else")
except Exception as e:
    print(f"Something Went Wrong: {e}")
    print("Something Went Wrong Check the code")
