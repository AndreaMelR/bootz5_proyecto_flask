from requests import request, session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def exchange():
    URL = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}'
    API_KEY = 'a8cf5d78-8dac-4325-838b-2ebe27f2f644'

    parameters = {
        'amount':'1',
        'symbol':'EUR',
        'convert':'BTC'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'API_KEY',
}
   
    #response = requests.get(URL.format(request.values.get('from_quantity'), request.values.get('from_currency'), request.values.get('to_currency'), API_KEY))
    session = session()
    session.headers.update(headers)

    try:
        response = session.get(URL, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        

       
    


