import my_module as m

try:
    while True:
       
        print("*"*70)
        m.banner()
        m.menu()
        print("*"*70)

        choice = int(input("Enter Your Choice Of Operation: "))
        m.validate_choice(choice)
        print("*"*70)

        match choice:
            case 1:
                m.createRecord()

            case 2:
                m.addNewRecord()
            
            case 3:
                m.viewRecords()

            case 4:
                m.delteRecords()

            case 5:
                print("The Whatsapp Function is still under development")
    
except ValueError:
    print("Enter Correct Choice")

except Exception as err:
    print("Some Error Occured: \n {err}")
