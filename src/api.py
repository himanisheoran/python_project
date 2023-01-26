from urllib.parse import quote_plus as url_encode
import requests

API_ENDPOINT = "HTTPS://FLIGHT.SUJAL.TECH/?oci={}&oco={}&dci={}&dco={}&dd={}"


def __generate_query_url(oci, oco, dci, dco, dd):
    return API_ENDPOINT.format(
        url_encode(oci),
        url_encode(oco),
        url_encode(dci),
        url_encode(dco),
        url_encode(dd)
    )


def __fetch_query(oci, oco, dci, dco, dd):
    url = __generate_query_url(oci, oco, dci, dco, dd)
    return requests.get(url).content.decode()


def get_tickets(oci, oco, dci, dco, dd):
    response = eval(__fetch_query(oci, oco, dci, dco, dd))
    if response["status"] == "success":
        tickets = response["tickets"]
        return tickets
    else:
        print("Server Error!")
        return []
