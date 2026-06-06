import asyncio

num = 0
async def incrementor():
    global num
    num += 1
    print(f"Incremented: {num}")

async def decrement():
    global num
    num -= 1
    print(f"Decremented: {num}")

async def main():
    tasks = []
    for _ in range(5):
        tasks.append(asyncio.create_task(incrementor()))
        tasks.append(asyncio.create_task(decrement()))

    await asyncio.gather(*tasks)
    print(f"Final value: {num}")

asyncio.run(main())