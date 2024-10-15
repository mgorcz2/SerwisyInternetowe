'''Przygotować program, który asynchronicznie pobiera treści z 5 różnych (dowolnych) stron internetowych w sposób współbieżny.'''

import aiohttp
import asyncio


async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.text())


async def main(*args) -> None:
    await asyncio.gather(*(fetch(url) for url in args))

if __name__ == "__main__":
    asyncio.run(main("http://wmii.uwm.edu.pl/","https://www.twojapogoda.pl/"))
