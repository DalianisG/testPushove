import http.client, urllib, os, pytz
from datetime import datetime


def pushoverFunction(): 
    tz = pytz.timezone("Europe/Athens")
    now = datetime.now(tz)
    current_time = now.strftime("%H:%M:%S")
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": os.environ["APP_TOKEN"],
        "user": os.environ["USER_KEY"],
        "message": "test notification, time is {}".format(current_time),
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

pushoverFunction()