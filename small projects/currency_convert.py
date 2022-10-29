import requests
import json

#Currency Converter
print("Use Currency abbreviations for the code to work properly")
#get currency the user is in
currency_in = input("what currency are you currently in? ")
money_in = int(input("What is the amount you have? "))
#get what currency the user wants
currency_out = input("what currency are you wanting? ")

#convert
url_part = 'https://api.exchangerate-api.com/v4/latest/'
url_combined = url_part + currency_in
response = requests.get(url_combined)
data = json.loads(response.text)

#print(type(data)) #dic

conversions = data['rates'][str(currency_out)]
money_out = money_in * conversions
print("The ammount in " + currency_out + " is " + str(money_out))