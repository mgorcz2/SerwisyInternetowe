'''Utworzyć aplikację, która będzie wykonywała się przez N sekund, co sekundę
wyświetlając kolejną liczbę ciągu Fibonacciego.'''

import asyncio

async def fib1(n):
    if n==0 or n==1:
        return n
    else:
        f1 = await fib1(n-1)
        f2 = await fib1(n-2)
        return f1+f2

async def printFib(n):
    for i in range(1,n+1):
        await asyncio.sleep(0.25)
        print(i, await fib1(i))

async def main():
    await printFib(6)
if __name__ == '__main__':
    asyncio.run(main())
