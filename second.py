import pymongo;

client = pymongo.MongoClient('localhost', 27017);

book_weather = client["weather"];

sheet_weather = book_weather["sheet_weather_6"];

for item in sheet_weather.find({"HeWeather6.basic.parent_city":"北京"}):
    print(item);