import asyncio
# in normal synchronous programming, one function executes after another irrespective predecessor being unproductive i.e waiting for data. Since during that time, cpu is not processing anything then the program wasting cpu time.
# in asynchoronous programming, any function being unproduction cause another function being executed in the place of predecessor. 
# it utilises idle cpu time

async def ab_print(): # async makes the function asynchoronous
    task = asyncio.create_task(c_print()) # create_task creates a function ref ig 
    print("A")
    await asyncio.sleep(3) # stops the function for few seconds
    print("B")
    await task # await tells the interpreter, hold it's execution horse till the function(task) finishes

async def c_print():
    print("C")
    await asyncio.sleep(1)
    print("D")
    await asyncio.sleep(4)
    print("E")



asyncio.run(ab_print())
