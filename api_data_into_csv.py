import requests
import csv

from requests.api import head

url= 'https://api.polygon.io/v2/snapshot/locale/global/markets/crypto/tickers?apiKey=rLkmkNvOMyH1KgnocknJb2owfqQGsJ7L'



headers = {'Accept':'application/json',
            'Content-Type':'application/json'
}


response =requests.request("GET", url, headers=headers,data={})
myjson=response.json()
ourdata=[]
csvheader=['TICKER','KOD']

for x in myjson['tickers']:
    listing=['ticker',x['ticker']]
    ourdata.append(listing)

with open ('ticker.csv','w',encoding='UTF8',newline='') as f:
    write=csv.writer(f)
    write.writerow(csvheader)
    write.writerows(ourdata)


print('done')
