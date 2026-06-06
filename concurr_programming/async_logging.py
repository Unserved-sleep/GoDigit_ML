import asyncio
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(filename='pyburger.log', level=logging.INFO)
task_queue = asyncio.Queue()

order_num = 0
closing = False

async def take_order():
   global order_num, closing
   try:
       order_num += 1
       logger.info(f"Taking Order #{order_num:04d}...")
       print(f"Order burger and fries for order #{order_num:04d}:")
       burger_num = await asyncio.to_thread(input, "Number of burgers:")
       for i in range(int(burger_num)):
           await task_queue.put(make_burger(f"{order_num:04d}-burger{i:02d}"))

       fries_num = await asyncio.to_thread(input, "Number of fries:")
       for i in range(int(fries_num)):
           await task_queue.put(make_fries(f"{order_num:04d}-fries{i:02d}"))

       logger.info(f"Order #{order_num:04d} queued.")
       print(f"Order #{order_num:04d} queued, please wait.")
       await task_queue.put(take_order())

   except ValueError:
       print("Goodbye!")
       logger.info("Closing down... stop taking orders and finish all tasks.")
       closing = True

async def make_burger(order_num):
   logger.info(f"Preparing burger #{order_num}...")
   await asyncio.sleep(5)  # time for making the burger
   logger.info(f"Burger made #{order_num}")

async def make_fries(order_num):
   logger.info(f"Preparing fries #{order_num}...")
   await asyncio.sleep(2)  # time for making fries
   logger.info(f"Fries made #{order_num}")

class Staff:
   def __init__(self, name):
       self.name = name

   async def working(self):
       while True:
           if task_queue.qsize() > 0:
               logger.info(f"{self.name} is working...")
               task = await task_queue.get()
               await task
               task_queue.task_done()
               logger.info(f"{self.name} finish task.")
           elif closing:
               return
           else:
               await asyncio.sleep(1) #rest

async def main():
   global task_queue
   task_queue.put_nowait(take_order())
   staff1 = Staff(name="John")
   staff2 = Staff(name="Jane")
   print("Welcome to Pyburger!")
   logger.info("Ready for business!")

   await asyncio.gather(staff1.working(), staff2.working())
   logger.info("All tasks finished. Closing now.")

if __name__ == "__main__":
   s = time.perf_counter()
   asyncio.run(main())
   elapsed = time.perf_counter() - s
   logger.info(f"Orders completed in {elapsed:0.2f} seconds.")