import asyncio
import time
async def f():
    print('Hello')
    time.sleep(0.1)
async def f2():
    await asyncio.sleep(0.1)
    await f()
    print('Goodbye')

asyncio.run(f2())

