import asyncio

'''Utwórz korutynę, która wyświetla wiadomość "Hello" po jednej sekundzie i "world" po dwóch sekundach.'''

async def oczekiwanie():
    await asyncio.sleep(1)
    print("Hello")
    await asyncio.sleep(2)
    print("World")

async def main():
    await oczekiwanie()

if __name__ == '__main__':
    asyncio.run(main())