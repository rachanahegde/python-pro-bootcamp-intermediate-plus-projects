import requests

TOKEN = ""
LOCATIONS_API_KEY = ""

sheety_endpoint = ""
locations_api_endpoint = "https://tequila-api.kiwi.com/locations/query"

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

locations_api_headers = {
    "Content-Encoding": "gzip",
    "apikey": LOCATIONS_API_KEY,
    "Accept": "application/json"
}


class DataManager:
    def __init__(self):
        self.cities_list = self.get_cities()
        self.iata_codes_list = self.get_iata_code()
        self.update_sheet()

    def get_cities(self):
        sheety_response = requests.get(url=sheety_endpoint, headers=bearer_headers)
        sheety_data = sheety_response.json()
        cities_list = [item['city'] for item in sheety_data['prices']]
        return cities_list

    def get_iata_code(self):
        iata_codes_list = []
        for city in self.cities_list:
            locations_params = {
                "term": city,
                "location_types": "city",
                "limit": 1
            }
            location_response = requests.get(url=locations_api_endpoint, params=locations_params,
                                             headers=locations_api_headers)
            location_data = location_response.json()
            iata_codes_list.append(location_data['locations'][0]['code'])
        return iata_codes_list

    def update_sheet(self):
        for num in range(len(self.cities_list)):
            update_sheet_endpoint = f"{sheety_endpoint}/{num + 2}"
            update_sheet_data = {
                "price": {
                    "iataCode": self.iata_codes_list[num]
                }
            }
            update_response = requests.put(url=update_sheet_endpoint, json=update_sheet_data,
                                           headers=bearer_headers)
            print(update_response.json())


# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
# with International Air Transport Association (IATA) codes for each city.
