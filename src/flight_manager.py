import pickle
from api import get_tickets
from datetime import datetime
from account_handler import account_exists


def __city_and_country_input(address_type):
    address = input(f"Enter {address_type} city, {address_type} country (seperated by comma): ").split(",")
    city, country = address
    is_valid_address = len(address) == 2 and (
        all([c.isalpha() or c.isspace() for c in city]),
        all([c.isalpha() or c.isspace() for c in country])
    )
    if is_valid_address:
        return city.strip(), country.strip()
    else:
        print("This input only allows spaces and alphabets, let's try again...")
        return __city_and_country_input(address_type)


def __date_input(date_type):
    date = input(f"Enter {date_type} date (dd/mm/yyyy): ")
    try:
        date = datetime.strptime(date, "%d/%m/%Y")
        return date.strftime("%d %B %Y")
    except ValueError:
        print("The date you entered is in invalid format, let's try again...")
        return __date_input(date_type)


def get_path():
    origin_city, origin_country = __city_and_country_input("origin")
    destination_city, destination_country = __city_and_country_input("destination")
    departure_date = __date_input("departure")
    return [
        origin_city, origin_country,
        destination_city, destination_country,
        departure_date
    ]


def get_user_data():
    account_file = open("account.dat", "rb")
    data = pickle.load(account_file)
    account_file.close()
    return data


def print_ticket(ticket):
    ad, dd = ticket["arrival_time"], ticket["departure_time"]
    printable = [
        "###############################",
        f"# From: {ticket['departure_airport']} -> To: {ticket['arrival_airport']}",
        f"# Leaves {dd['time']} on {dd['day']}, {dd['date']}",
        f"# Arrives {ad['time']} on {ad['day']}, {ad['date']}",
        f"# Total Duration: {ticket['total_duration']}",
        f"# Cost: {ticket['price']}",
        "###############################"
    ]
    padding = max([len(line) for line in printable])
    printable = [l + (" " * (padding - len(l))) + " #" for l in printable]
    printable[0] = printable[0].replace(" ", "#")
    printable[-1] = printable[-1].replace(" ", "#")
    print("\n", "\n".join(printable), "\n", sep="")


def search_flights():
    if not account_exists():
        print("Create account first to search flights.")
        return

    user, path = get_user_data(), get_path()
    tickets = get_tickets(*path)
    if tickets:
        for ticket in tickets:
            print_ticket(ticket)
    else:
        print("Unable to find tickets for given search parameters.")
