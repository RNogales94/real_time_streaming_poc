import datetime

import requests
import pandas as pd
from config import OPENWEATHERMAP_API_KEY
from typing import List


class DataGenerator():
    def __init__(self, api_key: str):
        self.api_key = api_key

    @staticmethod
    def __format_data(data: dict) -> List[dict]:
        lat = data.get("lat")
        lon = data.get("lon")
        tz_offset = data.get("timezone_offset")
        precipitation_pairs = data.get("minutely")
        result = []
        for pair in precipitation_pairs:
            dt = pair.get("dt")
            prec = pair.get("precipitation")
            result.append({
                "lat": lat,
                "lon": lon,
                "dt_CET": dt - tz_offset,
                "prec": prec,
            })
        return result

    def get_data(self, lat: float, lon: float) -> List[dict]:
        base_url = 'https://api.openweathermap.org/data/2.5'
        url = f'{base_url}/onecall?lat={lat}&lon={lon}&exclude=hourly,daily,current&units=metric&appid={self.api_key}'
        r = requests.get(url)
        return self.__format_data(r.json())


if __name__ == '__main__':
    api_key = OPENWEATHERMAP_API_KEY
    lat = 52.084516
    lon = 5.115539
    gen = DataGenerator(api_key=api_key)
    r = gen.get_data(lat, lon)

    print(r)
    print(pd.to_datetime(1644658140, unit='s', utc=True).tz_convert('Europe/Amsterdam'))
    print("...")
    print(pd.to_datetime(1644661980, unit='s', utc=True).tz_convert('Europe/Amsterdam'))
    print(len(r))