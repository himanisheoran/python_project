"""
THIS MODULE GETS USER INPUT FOR REGISTERING TICKET,
AND STORES INSIDE MYSQL DATABASE.
"""
import mysql.connector as sql

# ESTABLISHING CONNECTION TO MYSQL
connection = sql.connect(
    host="localhost",
    user="root",
    password="Sujal@5243",
    database="air_reservation"
)
c = connection.cursor()  # CREATING CURSOR OBJECT


def get_address():
    print("--- ENTER YOUR ADDRESS PLEASE ---")
    address = {
        "house_number": input("ENTER HOUSE NUMBER/APARTMENT: "),
        "floor_or_room": input("ENTER FLOOR/ROOM NUMBER: "),
        "address_line_1": input("ENTER ADDRESS LINE 1: "),
        "address_line_2": input("ENTER ADDRESS LINE 2 (OPTIONAL): "),
        "city": input("ENTER CITY: "),
        "state": input("ENTER STATE: "),
        "country": input("ENTER COUNTRY: "),
        "pin_code": input("ENTER PIN CODE: ")
    }

    # CHECKING IF ADDRESS IS VALID (NO ENTRY SHOULD BE EMPTY EXCEPT ADDRESS LINE 2)
    address_is_valid = False  # VALIDITY FLAG
    for key, val in address.items():
        if val == "" and key != "address_line_2":
            address_is_valid = False

    if address_is_valid:
        address["full_address"] = ", ".join(address.values())
        return address
    else:
        print("--- INVALID ADDRESS, PLEASE TRY AGAIN ---")
        get_address()


def get_seat_preference():
    print("--- SEAT PREFERENCE ---")

    print("CHOOSE YOUR ROW:",
          "1. LEFT",
          "2. MIDDLE",
          "3. RIGHT", sep="\n")

    while True:
        try:
            row_choice = int(input("ENTER ROW CHOICE: "))

            if row_choice == 1:
                row_choice = "left"
            elif row_choice == 2:
                row_choice = "middle"
            elif row_choice == 3:
                row_choice = "right"
            else:
                continue
            break
        except ValueError:
            print("INVALID INPUT, TRY AGAIN")

    print("CHOOSE SEAT LOCATION:",
          "1. WINDOW SEAT",
          "2. MIDDLE SEAT",
          "3. OUTERMOST SEAT", sep="\n")

    while True:
        try:
            seat_choice = int(input("ENTER ROW CHOICE: "))

            if seat_choice == 1:
                seat_choice = "window"
            elif seat_choice == 2:
                seat_choice = "middle"
            elif seat_choice == 3:
                seat_choice = "outermost"
            else:
                continue
            break
        except ValueError:
            print("INVALID INPUT, TRY AGAIN")

    return f"{row_choice}-{seat_choice}"


def get_luggage_weight():
    print("--- LUGGAGE WEIGHT ---")

    while True:
        try:
            weight = int(input("ENTER LUGGAGE WEIGHT IN KILOGRAMS: "))
            return weight
        except ValueError:
            print("INVALID INPUT, TRY AGAIN")


def get_ticket_info():
    return {
        "passenger_name": input("ENTER PASSENGER NAME: "),
        "address": get_address(),
        "mobile_no": input("ENTER YOUR MOBILE NUMBER: "),
        "destination": input("ENTER YOUR DESTINATION: "),
        "departure_time": input("ENTER YOUR DEPARTURE TIME: "),
        "seat_preference": get_seat_preference(),
        "luggage": get_luggage_weight()
    }
