import requests
import os
from PIL import Image
from datetime import date
from datetime import timedelta

API_KEY="DEMO_KEY"
BASE_URL="https://api.nasa.gov/planetary/apod"
storage_path=f"D:\\GIT REPO\\Python_Projects\\NasaApiUse\\Pics\\"

def getApod(date_today):
    apod_url=f"{BASE_URL}?api_key={API_KEY}&date={date_today}&thumbs=True"
    response=requests.get(apod_url)
    callsLeft=response.headers["X-RateLimit-Remaining"]
    print("Responses Left:- "+ callsLeft)
    data=response.json()
    if 'copyright' in data.keys() and int(callsLeft)>20:
        date_today=date_today-timedelta(days=1)
        print("FINDING NEW REQUEST of date ",date_today)
        getApod(date_today=date_today)
    else:
        info_pic=data["explanation"]
        hd_url_pic=data["hdurl"]
        datesss=data["date"]
        image=Image.open(requests.get(hd_url_pic,stream=True).raw)
        image.show()
        image=image.save(storage_path+f"APOD-{datesss}.jpg")
        print(info_pic)

getApod(date.today())