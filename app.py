from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=['POST', 'GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q': request.form.get("city"),
        'appid': request.form.get('appid'),
        'units': request.form.get('units')
    }

    response = requests.get(url, params=param) 
    data = response.json()

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'unit': 'Celsius',  # You can modify this based on the units parameter
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }

    return render_template("weather.html", **weather_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
