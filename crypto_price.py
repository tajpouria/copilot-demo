# Fetch the current price of a cryptocurrency from CoinMarketCap.

def fetch_price(crypto_name):
    import requests
    import json
    url = 'https://api.coinmarketcap.com/v1/ticker/' + crypto_name
    response = requests.get(url)
    data = json.loads(response.text)
    return data[0]['price_usd']

tar_crypto = input('Enter the name of the cryptocurrency: ')
price = fetch_price(tar_crypto)
print('The price of ' + tar_crypto + ' is $' + price)
