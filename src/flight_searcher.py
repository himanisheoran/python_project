from urllib.parse import quote_plus as url_encode
import requests

API_ENDPOINT = "HTTPS://FLY-SUJAL.HEROKUAPP.COM/?oci={}&oco={}&dci={}&dco={}&dd={}"
MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def get_tickets(search_data):
    query_url = API_ENDPOINT.format(*search_data)
    response = eval(requests.get(query_url).content.decode())
    if response["status"] == "success":
        tickets = response["tickets"]
        return tickets
    else:
        print("Unable to find tickets for given search parameters!")
        return []


def search_flights():
    pass
