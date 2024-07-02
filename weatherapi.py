from flask import Flask, render_template
import requests
app = Flask(__name__)

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