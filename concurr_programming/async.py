import asyncio
import time

async def make_burger(order_num):

    print(f"Preparing burger #{order_num}...")

    await asyncio.sleep(5) # time for making the burger

    print(f"Burger made #{order_num}")

async def main():

    order_queue = []

    for i in range(3):

        order_queue.append(make_burger(i))

    await asyncio.gather(*(order_queue))

if __name__ == "__main__":

    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s

    print(f"Orders completed in {elapsed:0.2f} seconds.")