import urllib.request
import json

APIKEY='WA06R1HHNMNPZZAR'

def getStockData(symbol):
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+symbol+'&apikey='+APIKEY
    connection=urllib.request.urlopen(url)
    return connection.read().decode()


def main():
    exit = False
    while(not exit):
        userinput = str(input("Enter a stock symbol or type quit to exit:"))
        if(userinput=="quit"):
            exit = True
        else:
            apiOutput = getStockData(userinput)
            output = json.loads(apiOutput)
            print("The current price of " + output['Global Quote']['01. symbol'] + " is " + output['Global Quote']['05. price'])
    print("Exiting program")

main()
