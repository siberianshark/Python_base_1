
from datetime import datetime
import requests


def currently_rates(currently_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):

    if not (currently_code and url):
        return None

    # fix register
    currently_code = currently_code.upper()

    # take respond from url
    respond = requests.get(url)

    if respond.ok:


        cur = respond.text.split(currently_code)

        if len(cur) == 1:


            return None

        # take value param from text
        value = cur[1].split("</Value>")[0].split("<Value>")[1]

        # conver to float
        value = float(value.replace(",", "."))

        # conver to decimal

        date = respond.headers['Date']
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()


        return (value, date)

    else:
        return None



print((currently_rates("Usd")))

print((currently_rates("eUR")))