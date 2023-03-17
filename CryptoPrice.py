# Modules
import requests
import time

# CoinMarketCap API Key

Coin_api = "Your_API_Key"

# Telegram BOT

token = "Your_Telegram_Bot_Token"
channel_id = "@YourChannelID" #OR Name ex. telegram.com/@example

# Requests web page
while True:

  url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY={Coin_api}'
  response = requests.get(url)

  # Get response content w/json() not .content

  Crypto = response.json()['data']
  # Crypto>>[]<< You can write the currency number as shown on the CoinMarketCap
  name = Crypto[1]['name']
  price = int(Crypto[1]['quote']['USD']['price'])
  message = f"{name} Price: {price}"
  print(message)
  send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + channel_id + '&text=' + message
  res = requests.get(send_text)
  # Time Sleep
  time.sleep(10 * 60)
