
# coding=utf-8
import requests;
import time;
import pymongo;

client = pymongo.MongoClient('localhost', 27017);

book_weather = client['weather'];

sheet_weather = book_weather['sheet_weather_6'];


url = 'https://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
strhtml.encoding = 'utf-8'

data = strhtml.text
data1 = data.split('\n')
for i in range(6):
    data1.remove(data1[0])

abc = []
for item in data1:
    print(item[2:13])
    abc.append(item[2:13])
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + \
        item[2:13].strip()+'&key=eb47202baeba458a877373dd6d94c867'
    strhtml = requests.get(url)
    strhtml.encoding = 'utf-8'
    time.sleep(1)

    dict = strhtml.json()

    sheet_weather.insert_one(dict);
    print(dict);
    # for item in dict['HeWeather6'][0]['daily_forecast']:
    #     print(item['tmp_max'])
