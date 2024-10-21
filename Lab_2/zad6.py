'''
Przygotować korutynę, która asynchronicznie pobierze prognozę pogody dla kilku wybranych miast, a następnie zwróci prognozy tylko dla tych miast, dla których prognoza
spełnia warunki przekazane w słowniku będącym maską filtrowania. Przykładowo, maska filtrowania zawierająca klucz wind_speed_10m o wartości < 20 pozostawi tylko te miasta,
które w prognozie pogody dla nadchodzących godzin będą miały przypisaną prędkośc wiatru o wartości < 20 km/h.
'''
from asyncio import gather

import aiohttp
import asyncio

async def fetch(city_name, latitude, longitude,mask):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,is_day,wind_speed_10m&timezone=Europe%2FBerlin"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            current_weather = data['current']['wind_speed_10m']
            for key,value in mask.items():
                if data['current'][key] > value:
                    return None
    return {city_name: f"wiatr: {current_weather}, temperatura: {data['current']['temperature_2m']}"}

async def main() -> None:
    maska = {'wind_speed_10m':20, 'temperature_2m': 30}     #filtrowanie dwoma kluczami
    data = await gather(
        fetch("Zakopane",49.299, 19.9489, maska),
        fetch("Porlamar", 10.9578,-63.8697, maska),
        fetch("Moroni", -11.7022, 43.2551, maska),
        fetch("Helsinki", -60.1695, 24.9354, maska)
    )
    weather_data = {}
    for result in data:
        if result is not None:
            weather_data.update(result)
    print(weather_data)

if __name__ == "__main__":
    asyncio.run(main())