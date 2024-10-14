'''Zadanie polega na symulacji harmonogramu pracy w fabryce, gdzie różne maszyny wykonują swoje zadania w ustalonych
przedziałach czasu. Maszyny muszą czekać na zakończenie poprzedniego cyklu zanim zaczną kolejny. Ustalić, aby każda
 maszyna działała w innym tempie, a wszystkie zadania były asynchroniczne. Każda maszyna ma swój cykl pracy, który
 powtarza się w określonym czasie (np. maszyna A – co 2 sekundy, maszyna B – co 3 sekundy, maszyna C – co 5 sekund).
Należy zasymulować ich działanie przez 15 sekund.'''
import asyncio
from asyncio import gather


async def tokarka(czas):
        start=0
        while start+2<= czas:
            await asyncio.sleep(2)
            print("##frezuje🟪")
            start += 2

async def piec(czas):
        start = 0
        while start+4 <= czas:
            await asyncio.sleep(3)
            print("##hartuje💢")
            start +=3


async def fabryka(czas):
    await asyncio.gather(
        tokarka(czas)
        ,piec(czas)
    )

asyncio.run(fabryka(6))
