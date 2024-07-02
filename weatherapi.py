from flask import Flask, render_template
import requests
app = Flask(__name__)

#Example URL: http://127.0.0.1:5000/hello/John

@app.route('/weather/<area>')
def get_weather(area):
    url = f"http://api.weatherapi.com/v1/forecast.json?key=b5970355f17d46098c6192412240207&q={area}&days=1&aqi=yes&alerts=yes"
    response = requests.get(url)
    if response.status_code == 400:
        return f"<h1>No information is available for {area}. Please enter another area.</h1>"
    info = response.json()
    name = info['location']['name']
    region = info['location']['region']
    temp = info['current']['temp_f']
    condition = info['current']['condition']['text']
    humidity = info['current']['humidity']
    feels_like = info['current']['feelslike_f']
    wind_speed = info['current']['wind_mph']
    gust_wind = info['current']['gust_mph']
    
    return render_template('index.html',name=name,region=region,temp=temp,condition=condition,humidity=humidity,feels_like=feels_like,wind_speed=wind_speed,gust_wind=gust_wind)

if __name__ == '__main__':
    app.run(debug=True)







#API Key: b5970355f17d46098c6192412240207

#GET requests to retrieve a list of posts


'''
['location']
{'name': 'Brooklyn', 'region': 'New York', 'country': 'USA', 'lat': 40.71, 'lon': -73.95, 'tz_id': 'America/New_York', 'localtime_epoch': 1719949637, 'localtime': '2024-07-02 15:47'}
['current']
{'last_updated_epoch': 1719949500, 'last_updated': '2024-07-02 15:45', 'temp_c': 28.9, 'temp_f': 84.0, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 3.8, 'wind_kph': 6.1, 'wind_degree': 60, 'wind_dir': 'ENE', 'pressure_mb': 1024.0, 'pressure_in': 30.24, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 27, 'cloud': 0, 'feelslike_c': 27.6, 'feelslike_f': 81.8, 'windchill_c': 28.0, 'windchill_f': 82.5, 'heatindex_c': 27.0, 'heatindex_f': 80.6, 'dewpoint_c': 8.4, 'dewpoint_f': 47.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 7.0, 'gust_mph': 9.8, 'gust_kph': 15.7, 'air_quality': {'co': 240.3, 'no2': 8.0, 'o3': 228.9, 'so2': 8.8, 'pm2_5': 23.3, 'pm10': 24.4, 'us-epa-index': 2, 'gb-defra-index': 2}}
 '''
