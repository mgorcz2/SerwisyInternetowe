'''Przygotować korutynę, która zwróci prognozę pogody dla najbliszej godziny dla miasta Zakopane. 
Wykorzystać w tym celu API Open-Meteo oraz przykładowy
 adres żądania: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,'''

import aiohttp
import asyncio

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast?latitude=49.299&longitude=19.9489&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1&forecast_hours=1"
    weather= await fetch(url)
    print(weather["hourly"]['temperature_2m'],"stopni celsjusza ")


if __name__ == "__main__":
    asyncio.run(main())