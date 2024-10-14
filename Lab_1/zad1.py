import asyncio

'''Utworzyć korutynę, która wstrzymuje działanie na 2 sekundy, a potem 
wyświetla komunikat o treści "Oczekiwanie zakończone".'''

async def oczekiwanie():
    await asyncio.sleep(2)
    print("oczekiwanie zakończone")

async def main():
    await oczekiwanie()

if __name__ == '__main__':
    asyncio.run(main())