import requests
import pandas as pd
from config import OPENWEATHERMAP_API_KEY

class DataGenerator():
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_data(self, lat: float, lon: float):
        base_url = 'https://api.openweathermap.org/data/2.5'
        url = f'{base_url}/onecall?lat={lat}&lon={lon}&exclude=hourly,daily,current&units=metric&appid={self.api_key}'
        r = requests.get(url)
        return r.json()


if __name__ == '__main__':
    api_key = OPENWEATHERMAP_API_KEY
    lat = 52.084516
    lon = 5.115539
    gen = DataGenerator(api_key=api_key)
    r = gen.get_data(lat, lon)

    print(pd.to_datetime(1644658080, unit='s', utc=True).tz_convert('Europe/Amsterdam'))
    print(pd.to_datetime(1644658140, unit='s', utc=True).tz_convert('Europe/Amsterdam'))
    print("...")
    print(pd.to_datetime(1644661980, unit='s', utc=True).tz_convert('Europe/Amsterdam'))
    print(len(r.get("minutely")))
