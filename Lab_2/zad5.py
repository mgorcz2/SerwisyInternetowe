'''
Przygotować korutynę, która pobierze współbieżnie prognozę pogody dla miast Porlamar, Moroni i Helsinek, a następnie zwróci
słownik zawierający klucze odpowiadające nazwom tych miast z wartościami prognozy pogody na najbliższą godzinę.
'''
import aiohttp
import asyncio

async def fetch(city_name, latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1&forecast_hours=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            current_weather = data['hourly']['temperature_2m']
            return {city_name: current_weather}


async def main() -> None:
    data = await gather(
        fetch("Zakopane",49.299, 19.9489),
        fetch("Porlamar", 10.9578,-63.8697),
        fetch("Moroni", -11.7022, 43.2551),
        fetch("Helsinki", -60.1695, 24.9354)
    )
    weather_data = {}
    for result in data:
        weather_data.update(result)
    print(weather_data)

if __name__ == "__main__":
    asyncio.run(main())