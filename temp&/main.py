import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -45
MY_LONG = 120

def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if (time_now.hour >= sunset) or (time_now.hour <= sunrise):
        return True
    else:
        return False


while True:
    time.sleep(5)
    if is_night() and is_close():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login("sender@gmail.com","passwd")
        connection.sendmail(from_addr="sender@gmail.com",to_addrs="reciever@gmail.com",msg="Subject:ISS Space Station\n"
                                                                                                  "ISS Space Station is over your head.")
        connection.close()