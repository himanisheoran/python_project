from account_handler import create_account, delete_account
from flight_manager import (
    search_flights
)


def menu():
    while True:
        print("###############################",
              "## WELCOME TO MUYAN AIRLINES ##",
              "## 1. SEARCH FLIGHTS         ##",
              "## 2. CREATE ACCOUNT         ##",
              "## 3. DELETE ACCOUNT         ##",
              "## 4. BOOK FLIGHT            ##",
              "## 5. CHECK BOOKED FLIGHTS   ##",
              "## 6. CANCEL FLIGHT          ##",
              "## 7. EXIT                   ##",
              "###############################", sep="\n")
        choice = input("Enter Choice: ")

        # SEARCH FLIGHTS
        if choice == "1":
            search_flights()

        # CREATE ACCOUNT
        elif choice == "2":
            create_account()

        # DELETE ACCOUNT
        elif choice == "3":
            delete_account()

        # BOOK FLIGHT
        elif choice == "4":
            pass

        # CHECK BOOKED FLIGHTS
        elif choice == "5":
            pass

        # CANCEL FLIGHT
        elif choice == "6":
            pass

        # EXIT
        elif choice == "7":
            print("--- We look forward to serve you again, goodbye! ---")
            break

        # INVALID CHOICE
        else:
            print("--- Sorry, that's not a valid choice. Let's try again... ---")


menu()
