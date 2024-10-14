'''Zadanie polega na symulowaniu kuchni, w której kilku kucharzy przygotowuje
 różne posiłki równocześnie. Każdy posiłek składa się z kilku etapów, np. krojenie warzyw,
 gotowanie makaronu, smażenie mięsa. Każdy etap trwa określony czas i jest realizowany asynchronicznie.
 Kucharze przygotowują trzy różne dania. Każde danie wymaga wykonania trzech kroków, które
 trwają różny czas (np. krojenie – 2 sekundy, gotowanie – 5 sekund, smażenie – 3 sekundy).'''

import asyncio
from asyncio import gather


async def frytki():
    await asyncio.sleep(2)
    print("-pokroilem frytki")
    await asyncio.sleep(3)
    print("--przyprawilem frytki")
    await asyncio.sleep(2)
    print("---usmazylem frytki")
    print("----wydaje frytki🍟---")

async def kurczak():
    await asyncio.sleep(5)
    print("-pokroilem kurczaka")
    await asyncio.sleep(3)
    print("--kurczaka posypalem")
    await asyncio.sleep(7)
    print("---usmazylem kurczaka")
    print("----wydaje kurczaka🐔---")

async def brokul():
    await asyncio.sleep(1)
    print("-umylem brokul")
    await asyncio.sleep(2)
    print("--uparowalem brokul")
    await asyncio.sleep(1)
    print("---przyprawilem brokul")
    print("----wydaje brokul🥦---")

async def danie(*args):
    await gather(*args)
    await asyncio.sleep(3)
    print("💯------Wydaje gotowe danie🍝-----")

asyncio.run(danie(kurczak(),brokul(),frytki()))