'''Zadanie polega na symulowaniu przetwarzania pięciu dużych plików, gdzie każdy plik musi przejść przez kilka etapów przetwarzania, t
akich jak wczytanie, analiza i zapis. Każdy z tych kroków trwa określony czas i musi być wykonany asynchronicznie.
Każdy plik przechodzi przez trzy etapy: wczytanie (2 sekundy), analiza (4 sekundy), zapis (1 sekunda).
Symuluj asynchroniczne przetwarzanie wszystkich plików naraz.'''

import asyncio
from asyncio import gather


async def przetworz_plik(plik):
    print("-wczytuje ",plik)
    await asyncio.sleep(2)
    print("--analizuje ",plik)
    await asyncio.sleep(4)
    print("---zapisuje ",plik)
    await asyncio.sleep(1)

async def load_files(*args):
    await gather(*(przetworz_plik(plik) for plik in args))

asyncio.run(load_files("Plik1","Plik2","Plik3","Plik4","Plik5"))