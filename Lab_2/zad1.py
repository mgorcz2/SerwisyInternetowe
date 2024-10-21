'''Przygotować korutynę, która asynchronicznie pobiera i zwraca zawartość strony internetowej z podanego adresu URL przy użyciu biblioteki aiohttp.'''

import aiohttp
import asyncio

async def fetch(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.text())


async def main() -> None:
    await fetch("https://uwm.edu.pl")


if __name__ == "__main__":
    asyncio.run(main())
