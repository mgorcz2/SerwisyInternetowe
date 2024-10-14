import asyncio
'''Utworzyć dwie korutyny, a następnie je uruchomić współbienie. 
Obie korutyny będą miały takie samo działanie: oczekują zadaną ilość czasu, a następnie 
wyświetlają komunikat. Niech pierwsza z nich czeka trzy sekundy, a druga jedną sekundę.'''

async def ko1():
    await asyncio.sleep(3)
    print("Ko1")

async def ko2():
    await asyncio.sleep(1)
    print("Ko2")

async def main():
    await asyncio.gather(ko1(), ko2()) #wspolbiezne uruchomienie, ko2 skonczy pierwsze

if __name__ == '__main__':
    asyncio.run(main())