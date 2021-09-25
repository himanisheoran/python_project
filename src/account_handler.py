import os
import pickle


def __get_user_data():
    data = {}
    while True:
        name = input("Enter your name: ")
        is_valid_name = False not in [c.isalpha() or c == " " for c in name]
        if is_valid_name:
            data["name"] = name
            break
        else:
            print("Names only contain alphabets and spaces, try again...")

    while True:
        number = input("Enter your phone number: ")
        is_valid_number = len(number) == 10 and number.isdigit()
        if is_valid_number:
            data["number"] = number
            break
        else:
            print("This isn't a valid number, please try again...")

    while True:
        cc_number = input("Enter credit card number (16 digits): ")
        cvv = input("Enter cvv: ")
        is_valid_card = len(cvv) + len(cc_number) == 19 and cvv.isdigit() and cc_number.isdigit()
        if is_valid_card:
            data["card"] = (cc_number, cvv)
            break
        else:
            print("This isn't a a valid card, let's try again...")
    return data


def __account_exists():
    try:
        open("account.dat").close()
        return True
    except FileNotFoundError:
        return False


def create_account():
    if __account_exists():
        print("Account already exists! Delete current account to create new.")
        return

    account_file = open("account.dat", "wb")
    pickle.dump(__get_user_data(), account_file)
    account_file.close()
    print("Account created!")


def delete_account():
    os.remove("account.dat")
    print("Account Deleted!")
