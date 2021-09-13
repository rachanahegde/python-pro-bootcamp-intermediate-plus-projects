import requests
import datetime as dt

TOKEN = ""
KIWI_API_KEY = ""

sheety_endpoint = ""
flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

flight_api_headers = {
    "Content-Encoding": "gzip",
    "apikey": KIWI_API_KEY,
    "Accept": "application/json"
}

tomorrow = dt.date.today() + dt.timedelta(days=1)
formatted_tomorrow = tomorrow.strftime("%d/%m/%Y")
six_months_later = tomorrow + dt.timedelta(weeks=24)
formatted_six_months_later = six_months_later.strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self):
        self.sheety_data = self.get_data()
        self.flight_data_list = self.flight_search()

    def get_data(self):
        # sheety_response = requests.get(url=sheety_endpoint)
        # sheety_data = sheety_response.json()
        # return sheety_data['prices']

        # Hard coded data from google sheets below to avoid using up requests quota for google sheets API.
        city_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                     {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
                     {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
                     {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
                     {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
                     {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
                     {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
                     {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
                     {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10},
                     {'city': 'Bali', 'iataCode': 'DPS', 'lowestPrice': 501, 'id': 11}]
        return city_data

    def flight_search(self):
        flight_data_list = []
        for item in self.sheety_data:
            flight_search_params = {
                "fly_from": "LON",
                "fly_to": item['iataCode'],
                "date_from": formatted_tomorrow,
                "date_to": formatted_six_months_later,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "price_to": item['lowestPrice'],
                "max_stopovers": 0,
                "curr": "GBP",
            }
            flight_response = requests.get(url=flight_search_endpoint, params=flight_search_params,
                                           headers=flight_api_headers)
            flight_data = flight_response.json()['data']
            if flight_data:
                flight_data_list.append(flight_data[0])
            else:
                flight_search_params["max_stopovers"] = 1
                flights_with_stopover_response = requests.get(url=flight_search_endpoint, params=flight_search_params,
                                                              headers=flight_api_headers)
                stopover_data = flights_with_stopover_response.json()['data']
                if stopover_data:
                    flight_data_list.append(stopover_data[0])
        return flight_data_list
