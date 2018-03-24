import asyncio
import time

async def outer():
    print("in outer")
    print("waiting for result 1")
    result1 = await phase1()

    print("waiting for result 2")
    result2 = await phase2()
    return(result1, result2)

async def phase1():
    print("in phase1")
    time.sleep(4)
    return "result1"

async def phase2():
    print("in phase2")
    time.sleep(1)
    return "result2"

event_loop=asyncio.get_event_loop()

try:
    return_value = event_loop.run_until_complete(outer())
    print("return_value {}".format(return_value))
finally:
    event_loop.close()

