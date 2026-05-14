from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
station = pd.read_csv("data_small/stations.txt", skiprows=17)
station.columns = station.columns.str.strip()
station = station.drop(["CN", "LAT" ,"LON", "HGHT"], axis=1)
station = station.to_html()

@app.route("/")
def home():
    return render_template("home.html", data = station)

@app.route("/api/v1/<station>/")
def weather_stations(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    station_data = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    station_data.columns = station_data.columns.str.strip()
    return station_data.to_dict(orient="records")


@app.route("/api/v1/<station>/<date>/")
def weather(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df.columns = df.columns.str.strip()
    temperature = df.loc[df["DATE"] == date]["TG"].squeeze()/10
    temperature = str(temperature)
    return {"station": station,
            "date": date,
            "temperature": temperature,
            "filename": filename}

@app.route("/api/v1/yearly/<station>/<year>/")
def yearly_station(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df.columns = df.columns.str.strip()
    df["DATE"] = pd.to_datetime(df["DATE"], format="%Y%m%d")
    result = df[df["DATE"].dt.year == int(year)]
    result = result.to_dict(orient="records")
    return result




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
