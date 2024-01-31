import mysql.connector

# Replace these with your own database details
host = 'host'
username = 'username'
password = 'password'
database = 'database'

try:
    conn = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    cursor = conn.cursor()

except mysql.connector.Error as err:
    print(f"Error: {err}")

class Hotel:
    def __init__(self):
        print("Welcome to the Hotel Booking App!")
        inp = input("\nDo you want to register with us or login? Type 1 for register/login: ")
        if inp == "1":
            self.registration()
        else:
            print("\nYou have entered an wrong option, please enter correct given option")
            Hotel()

    def registration(self):
        user_email_id = input("Please enter your email id: ").lower()
        cursor.execute(f"SELECT * FROM hotelinfor WHERE user_email_id = '{user_email_id}'")
        user_email = cursor.fetchone()
        if user_email:
            print("\nYou already registered with us")
            password = input("\nPlease enter your password: ")
            cursor.execute(f"SELECT * FROM hotelinfor WHERE password = '{password}'\n")
            user_password = cursor.fetchone()
            if user_password:
                cursor.execute(f"SELECT user_fname, user_lname FROM hotelinfor WHERE user_email_id = '{user_email_id}'")
                fname, lname = cursor.fetchone()
                print(f"\nWelcome to the Hotel Booking App {fname.capitalize()} {lname.capitalize()}!!")
                self.selection(user_email_id)
            else:
                print("\nYou have entered an incorrect password, please enter your password correctly")
                fp = input("\nForgot password? Do you want to change it? Type 1 or Type 2 for try again:  ")
                if fp == '1':
                    new_password = input("\nPlease enter your new password: ")
                    cursor.execute(f"update hotelinfor set password = '{new_password}' where user_email_id = '{user_email_id}'")
                    conn.commit()
                    print("\nYour password has been changed!")
                    cursor.execute(f"SELECT user_fname, user_lname FROM hotelinfor WHERE user_email_id = '{user_email_id}'")
                    fname, lname = cursor.fetchone()
                    print(f"\nWelcome to the Hotel Booking App {fname.capitalize()} {lname.capitalize()}!")
                    self.booking(user_email_id)
                else:
                    self.registration()
        else:
            user_fname = input("Please enter your first name: ").lower()
            user_lname = input("Please enter your last name: ").lower()
            password = input("Please enter your password: ").lower()

            cursor.execute("INSERT INTO hotelinfor (user_email_id, user_fname, user_lname, password) VALUES (%s, %s, %s, %s)",
                           (user_email_id, user_fname, user_lname, password))
            conn.commit()
            print("\nRegistration successful!")
            print(f"\nWelcome to the Hotel Booking App {user_fname.capitalize()} {user_lname.capitalize()}!")
            self.selection(user_email_id)


    def selection(self, user_email_id):

        book_hotel_city_name = input("Please enter the city name, where you want to book the hotel?: ").lower()
        from_date = input("Please enter date, on which you want to book hotel? 'YYYY-MM-DD': ")
        to_date = input("Please enter the IN time, on which time you want to book the hotel? 'HH:MM:SS': ")
        no_of_room = int(input("Please enter how many room you want to book?: "))
        no_of_guest = int(input("Please enter how many guest?: "))

        print(f"\nBooking details are accepted, checking hotel's availability in {book_hotel_city_name}..")

        print("\nHere are the below list of available hotel's rooms \n")
        cursor.execute("SELECT hotel_name, city_name, state_name, hotel_area_name, hotel_address, hotel_pincode, per_day_room_price FROM hotel_info WHERE city_name = %s", (book_hotel_city_name,))
        rooms = cursor.fetchall()

        if rooms:
            print(f"\nAvailable Rooms in {book_hotel_city_name}:")
            print("-" * 100)
            for room in rooms:
                print(f"Hotel Name: {room[0]}")
                print(f"City: {room[1]}, {room[2]}")
                print(f"Area Name: {room[3]}")
                print(f"Address: {room[4]}")
                print(f"Pincode: {room[5]}")
                print(f"Price: ${room[6]} per day")
                print("\nAs per the selection you made earlier:")
                total_cost = no_of_room * no_of_guest * room[6]
                print(f"{no_of_room} Room * {no_of_guest} Guest * ${room[6]} Price\nFinal Price = ${total_cost}")
                print("-" * 100)
            self.booking(no_of_room, no_of_guest)
        else:
            print(f"\nNo available rooms in {book_hotel_city_name}.")
            self.selection(user_email_id)
        
    def booking(self, no_of_room, no_of_guest):

        hotel = input(f"\nPlease enter the Hotel name you want confirm booking: ").lower()
        if hotel:
            cursor.execute("SELECT hotel_name, city_name, state_name, hotel_area_name, hotel_address, hotel_pincode, per_day_room_price FROM hotel_info WHERE hotel_name = %s", (hotel,))
            user_select = cursor.fetchall()
            print("------------ Receipt --------------\n")
            for final_hotel in user_select:
                print(f"Hotel Name: {final_hotel[0]}")
                print(f"City: {final_hotel[1]}, {final_hotel[2]}")
                print(f"Area Name: {final_hotel[3]}")
                print(f"Address: {final_hotel[4]}")
                print(f"Pincode: {final_hotel[5]}")
                print(f"Price: ${final_hotel[6]} per day")
                print("\nAs per the selection you made earlier:")
                total_cost = no_of_room * no_of_guest * final_hotel[6]
                print(f"{no_of_room} Room * {no_of_guest} Guest * ${final_hotel[6]} Price\nTotal Price Paid = ${total_cost}")
            print("-----------------------------------\n")
            print("\nThank You!")
            inn = input("\nDo you want to book another ticket type 1 or go back to booking page type 2")
            if inn == "1":
                self.selection()
            else:
                self.booking(no_of_room, no_of_guest)
        else:
            print("\nPlease enter correct Hotel name")
            self.booking(no_of_room, no_of_guest)
Hotel()