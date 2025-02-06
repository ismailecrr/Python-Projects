import requests

url="https://www.oanda.com/currency-converter/en/?from=EUR&to=USD&amount=1"

birinci_döviz=input("birinci döviz:")
ikinci_döviz=input("ikinci döviz:")

response=requests.get(url+birinci_döviz)
json_verisi=response.json()

print(json_verisi)