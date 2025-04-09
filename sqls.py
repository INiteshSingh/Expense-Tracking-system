import mysql.connector
"""This Modlue Contains the code for performing operations on the sql data base"""
def alter_data_base():
        try:
                print("*"*70)
                print("\tAltering Table A2_ITEMS")
                print("*"*70)
                db_config = {
                "host": "maglev.proxy.rlwy.net",  # Replace with actual IP or localhost if needed
                "user": "root",
                "password": "mfcfnwwTVmVbvRbzOZlfeIIWrLEhSwrk",  # Replace with your password
                "database": "railway",  # Ensure this is the correct database name
                "port": 21724  # Ensure this is an integer
                }

                print("🔌 Trying and Connecting to Railway MySQL...")
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                print("✅ Successfully Connected!")

                sql = input("Enter Your SQL QUERY to Modify The Tabel").strip()
                
                cursor.execute(sql)
                conn.commit()
                print("✅ Table Altered Successfully!")

                cursor.close() 
                conn.close()
                
        except ValueError:
                print("Enter Correct Values for item Details")
        except mysql.connector.Error as err:
                print(f"Database error: {err}")
        except Exception as e:
                print(f"Error Occured : {e}")

def add_data():
        try:
                print("*"*70)
                print("\tAdding Table Data")
                print("*"*70)
                
                
              #  ✅ Database credentials — replace with your Railway values| Remove the hashtags when using the function 
                db_config = {
                "host": "maglev.proxy.rlwy.net",  # Replace with actual IP or localhost if needed
                "user": "root",
                "password": "mfcfnwwTVmVbvRbzOZlfeIIWrLEhSwrk",  # Replace with your password
                "database": "railway",  # Ensure this is the correct database name
                "port": 21724  # Ensure this is an integer
                }
        #mysql://root:ONGxOqFzIDdqDpHpSMsaIsBffkNfXvHW@gondola.proxy.rlwy.net:34598/railway

                print("🔌 Connecting to Railway MySQL...")
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                print("✅ Successfully connected!")

                item_name = input("Enter Item Name to store in the database: ").strip()
                item_price = float(input("Enter Item Price: "))

                sql = """INSERT INTO A2_ITEMS (item_name,item_price)
                        VALUES (%s, %s)"""
                values = (item_name, item_price)

                cursor.execute(sql,values)
                conn.commit()
                print("✅ Data Inserted Successfully!")

                cursor.close()
                conn.close()
                
        except ValueError:
                print("Enter Correct Values for item Details")
        except mysql.connector.Error as err:
                print(f"Database error: {err}")
        except Exception as e:
                print(f"Error Occured : {e}")

#This Works Just Fine as long as the railway.app's data base is active 
#But Now the Question is that how would i enter Such large amount of items data into the data base

#FastForward Next day found the solution, have to use csv files which were initially excel files where i entered data manually
#Creating a function today to write the data into the db using a csv file 
add_data()