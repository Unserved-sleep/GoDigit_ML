import asyncio
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='cncr',
    filemode='w',   # overwrite each run
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
lock = asyncio.Lock()
num = 0

async def increment():
    global num
    async with lock:
        num += 1
        logging.info(f"Incremented: {num}")
        print(f"Incremented: {num}")

async def decrement():
    global num
    async with lock:
        num -= 1
        logging.info(f"Decremented: {num}")
        print(f"Decremented: {num}")

async def main():
    tasks = []
    logger.info("Starting main")

    for i in range(10):
        tasks.append(increment())
        tasks.append(decrement())
    await asyncio.gather(*tasks)
    print(f"Incremented: {num}")
    logging.info("Finished main")

asyncio.run(main())