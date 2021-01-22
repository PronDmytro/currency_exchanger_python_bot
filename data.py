import requests
from config import URL
from datetime import datetime

response = requests.get(URL).json()
currency_code = {'usd': 840, 'eur': 978, 'rub': 643, 'pln': 985}


def course(code):
    if code == 'usd':
        return usd
    elif code == 'eur':
        return eur
    elif code == 'rub':
        return rub
    elif code == 'pln':
        return pln


class Currency:
    def __init__(self, buy, sell, date, code):
        self.buy = buy
        self.sell = sell
        self._date = datetime.fromtimestamp(date)
        self.code = code

    def __str__(self):
        return f"Курс валюти {self.code}: \n💰 Курс продажі: {self.sell}\n💰Курс купівлі: {self.buy}\nСтаном на: {self._get_str_date()} "

    def _get_str_date(self):
        return f"{self._date.day}.{self._date.month}.{self._date.year}"

    def exchange_from(self, value):
        return round(value / self.buy, 2)

    def exchange_to(self, value):
        return round(self.sell * value, 2)


usd = Currency(buy=response[0]['rateBuy'],
               sell=response[0]['rateSell'],
               date=response[0]['date'],
               code=response[0]['currencyCodeA'])
eur = Currency(buy=response[1]['rateBuy'],
               sell=response[1]['rateSell'],
               date=response[1]['date'],
               code=response[1]['currencyCodeA'])
rub = Currency(buy=response[2]['rateBuy'],
               sell=response[2]['rateSell'],
               date=response[2]['date'],
               code=response[2]['currencyCodeA'])
pln = Currency(buy=response[4]['rateBuy'],
               sell=response[4]['rateSell'],
               date=response[4]['date'],
               code=response[4]['currencyCodeA'])
