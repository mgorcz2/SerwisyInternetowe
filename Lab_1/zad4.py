'''Utworzyć aplikację, która co sekundę wyświetla kolejne liczby od 1 do 5.
Należy pamiętać o zastosowaniu podejścia asynchronicznego!'''

import asyncio

async def licz():
    for i in range(1,6):
        print(i)
        await asyncio.sleep(1)

async def main():
    await licz()

if __name__ == '__main__':
    asyncio.run(main())