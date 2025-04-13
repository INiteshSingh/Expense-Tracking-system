import my_module as m

try:
    while True:
       
        print("*"*70)
        m.banner()
        m.menu()
        print("*"*70)

        choice = int(input("Enter Your Choice Of Operation: "))
        print("*"*70)

        match choice:
            case 1:
                m.create_new_db()

            case 2:
                m.create_new_table()
            
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
    print(f"Some Error Occured: \n {err}")
