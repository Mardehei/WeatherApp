from flask import Flask, request, render_template
import requests
import urllib

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    data = ''
    error = 0
    city = ''
    if request.method == "POST":
        city = request.form.get("cityName")
        if city:
            weatherApi = '7e491f82ad6ab793e093d82c83936de2'
            url = "https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid=" + weatherApi
            data = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data=data, cityName=city, error=error)


if __name__ == "__main__":
    app.run()
