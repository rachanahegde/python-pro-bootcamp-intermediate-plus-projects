from twilio.rest import Client
import smtplib
import requests

account_sid = ""
auth_token = ""

MY_EMAIL = ""
MY_PASSWORD = ""
MY_PHONE_NUMBER = ""
TWILIO_NUMBER = ""

users_sheet_endpoint = ""


class NotificationManager:
    def __init__(self, flight_data_list):
        self.flight_data_list = flight_data_list
        self.structure_message()

    def structure_message(self):
        for item in self.flight_data_list:
            departure_airport_code = item["flyFrom"]
            destination_airport_code = item["flyTo"]
            departure_city = item["cityFrom"]
            destination_city = item["cityTo"]
            flight_price = item["price"]
            outbound_flight_date = item["route"][0]["local_departure"]
            formatted_outbound_date = outbound_flight_date.split("T")[0]
            inbound_flight_date = item["route"][len(item["route"])-1]["local_departure"]
            formatted_inbound_date = inbound_flight_date.split("T")[0]

            flight_deal_message = f"Low price alert! Only £{flight_price} to fly "\
                                  f"from {departure_city}-{departure_airport_code} "\
                                  f"to {destination_city}-{destination_airport_code}, "\
                                  f"from {formatted_outbound_date} to {formatted_inbound_date}."

            if len(item["route"]) > 2:
                flight_deal_message += f"\nFlight has 1 stop over, via {item['route'][0]['cityTo']}."

            # self.send_text(flight_deal_message)

            flight_deal_message += f"\n https://www.google.co.uk/flights?hl=en#flt=" \
                                   f"{departure_airport_code}.{destination_airport_code}.{formatted_outbound_date}*" \
                                   f"{item['routes'][1][0]}.{item['routes'][1][1]}.{formatted_inbound_date}"
            self.send_emails(flight_deal_message)

    def send_text(self, flight_deal_message):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=flight_deal_message,
            from_=TWILIO_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(message.body)

    def send_emails(self, flight_deal_message):
        users_response = requests.get(url=users_sheet_endpoint)
        user_data = users_response.json()['users']

        for user in user_data:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user['email'],
                    msg=f"Subject:New Low Price Flight!\n\n"
                        f"{flight_deal_message}".encode('utf-8')
                )

