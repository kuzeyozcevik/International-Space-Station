# International-Space-Station
This Python script tracks the International Space Station (ISS) in real time using public APIs and notifies you via email when the ISS is flying over your location at night.

It uses the Open Notify ISS API to get live ISS coordinates

Determines day/night status using the Sunrise–Sunset API

Sends automated email alerts using Python’s smtplib library

The script continuously checks whether the ISS is within ±5° of your latitude and longitude and whether it is currently night at your location. When both conditions are met, it sends you an email notification so you don’t miss the sighting.


![image](https://github.com/kuzeyozcevik/International-Space-Station/blob/c6dba94ae25c0e1345823e32df2820adff4af319/photo/iss.jpeg)
![image](https://github.com/kuzeyozcevik/International-Space-Station/blob/c6dba94ae25c0e1345823e32df2820adff4af319/photo/iss.png)

