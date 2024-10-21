'''
Przygotować program, który asynchronicznie pobierze plik binarny za pomocą wskazanego URL (np. obraz, wideo, nagranie) z sieci, a następnie zapisze go na dysku lokalnym pod wskazaną ścieżką.
'''
from asyncio import gather

import aiohttp
import asyncio


async def download_file(url, save_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(save_path, 'wb') as f:
                f.write(await response.read())
            print(f"Pobrano")


async def main() -> None:
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.haloart.pl%2Fjoanna-podolska%2Fobrazy-akryl%2Fkogut-realistyczny-obraz-akrylowy%2C115485.html&psig=AOvVaw0k6Z5LoKWiF3d1R_6mk19E&ust=1729609837318000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjRh_Xgn4kDFQAAAAAdAAAAABAJ"
    save_path = "C:/users/Marcin/Desktop"
    await download_file(url, save_path)


if __name__ == "__main__":
    asyncio.run(main())
