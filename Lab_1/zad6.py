'''Utworzyć aplikację, która będzie symulowała pobieranie danych z innych usług sieciowych.
 W tym celu należy utworzyć korutynę fetch(delay: int), która po odczekaniu delay sekund
 zwróci dowolną wartość (symulacja pobierania danych z sieci). Następnie należy kilkukrotnie
  wywołać współbieżnie korutynę fetch z różnymi wartościami parametru delay. Podpowiedź: do
  współbieżnego wywołania wielu korutyn można wykorzystać funkcję gather, która zostanie
   umieszczona w dedykowanej korutynie. Wówczas nie ma potrzeby stosowania manualnego
    podejścia zarządzania zadaniami oraz pętlą zdarzeń.'''

import asyncio
from asyncio import gather


async def fetch(delay) -> None:
    await asyncio.sleep(delay)
    print(delay, "Dane")

async def main():
    await gather(fetch(4), #3
                 fetch(5), #4
                 fetch(2), #1 kolejnosc
                 fetch(3)) #2

if __name__ == '__main__':
    asyncio.run(main())
