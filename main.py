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
                m.createDatabase()

            case 2:
                m.create_table_in_db()
            
            case 3:
                m.addNewRecord()

            case 4:
                m.delteRecords()

            case 5:
                print("The Whatsapp Function is still under development")

            case _:
                print("Not a Valid input")
except ValueError:
    print("Enter Correct Choice")

except Exception as err:
    print("Some Error Occured: \n {err}")
