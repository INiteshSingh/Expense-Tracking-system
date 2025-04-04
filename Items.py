# Program to Add data to the Store_items_list table in the Railway MySQL database
import mysql.connector

def add_data():
    try:
        item_id = int(input("Enter Item ID: "))
        item_name = input("Enter Item Name to store in the database: ").strip()
        item_price = float(input("Enter Item Price: "))  # Now allows decimals

        # ✅ Database credentials — replace with your Railway values
        db_config = {
            "host": "gondola.proxy.rlwy.net",  # Replace with your actual host
            "user": "root",                      # Replace with your username
            "password": "ONGxOqFzIDdqDpHpSMsaIsBffkNfXvHW",                  # Replace with your password
            "database": "railway",                        # Replace with your DB name
            "port": 34598                                   # Must be an integer
        }
#mysql://root:ONGxOqFzIDdqDpHpSMsaIsBffkNfXvHW@gondola.proxy.rlwy.net:34598/railway
        print("🔌 Connecting to Railway MySQL...")
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        print("✅ Successfully connected!")

        # ✅ SQL Insert Query
        sql = """
        INSERT INTO Store_items_list (id, Item_name, Item_price)
        VALUES (%s, %s, %s)
        """
        values = (item_id, item_name, item_price)

        cursor.execute(sql, values)
        conn.commit()
        print(f"✅ Successfully inserted: {values}")

        cursor.close()
        conn.close()

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers for ID and Price.")

    except mysql.connector.Error as err:
        print(f"❌ MySQL Error: {err}")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

add_data()

#This Works Just Fine as long as the railway.app's data base is active 
#But Now the Question is that how would i enter Such large amount of items data into the data base
