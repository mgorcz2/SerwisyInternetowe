import asyncio
 #---- await - rozpoczynamy koprocedure(wrzucamy ją do pętli)
async def pobieraj_dane():
    print('zaczynam pobieranie')
    await asyncio.sleep(2) #czekam 2 sek
    print('skonczylem pobieranie')
    return {'dane' : 1}

async def licznik():
    for i in range (10):
        print(i)
        await asyncio.sleep(0.50)

async def main():
    task1 = asyncio.create_task(pobieraj_dane()) #pierwsze zadanie to zebranie danych,
    # jesli by nie było task1, tylko samo "await pobieraj_dane()" to task2 by musial czekac az to sie skonczy
    task2 = asyncio.create_task(licznik()) #drugie zadanie to liczenie
        #--------taski są potrzebne, jesli chcemy zarządzac wątkami asynchronicznymi

    value = await task1  #value (future - 'obietnica ze cos tam bedzie') to wynik pierwszego zadania
    print(value)
    await task2 #jesli tego nie bedzie to nie skonczy drugiego zadania

if __name__ == '__main__':
    asyncio.run(main())

'''     wynik:
zaczynam pobieranie
0
1
2
3
skonczylem pobieranie
4
{'dane': 1}
5
6
7
8
9
'''