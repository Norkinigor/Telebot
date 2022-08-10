import decimal
import json
import requests
from config import exchanges

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        
        try:
            amount = decimal(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        
        r = requests.get(f"https://api.exchangerate.host/latest?base={base_key}&symbols={quote_key}")
        requests.get(..., timeout=...)
        r.raise_for_status()

        resp = json.loads(r.content)
        new_price = resp['rates'][quote_key] * amount
        new_price = round(new_price, 3)
        message =  f"Цена {amount} {base} в {quote} : {new_price}"
        return message
