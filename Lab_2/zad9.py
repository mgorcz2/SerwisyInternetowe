'''
Przygotować program, który wyśle asynchronicznie 100 żądań do dowolnego
REST API i zachowa tylko te odpowiedzi, które mają kod statusu odpowiedzi w
zakresie 200-299. W przypadku błędu serwera (kody 500-599), powinien
ponowić próbę wysłania żądania maksymalnie 3 razy.
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
    return {city_name: current_weather}

async def main() -> None:
    maska = {}     #filtrowanie dwoma kluczami
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
    print(sorted(weather_data.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    asyncio.run(main())