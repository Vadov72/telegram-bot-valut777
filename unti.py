import json
import requests
from config import keys


class ConvertiException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertiException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertiException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertiException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertiException(f'Не удалось обработать количество')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]


        return total_base



