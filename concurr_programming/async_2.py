import asyncio
import time

order_queue = asyncio.Queue()

def take_order():
  for i in range(3):
      order_queue.put_nowait(make_burger(i))

async def make_burger(order_num):
  print(f"Preparing burger #{order_num}...")
  await asyncio.sleep(5)  # time for making the burger
  print(f"Burger made #{order_num}")

class Staff:
  def __init__(self, name):
      self.name = name

  async def working(self):
      while order_queue.qsize() > 0:
          print(f"{self.name} is working...")
          task = await order_queue.get()
          await task
          print(f"{self.name} finished a task...")

async def main():
  staff1 = Staff(name="John")
  staff2 = Staff(name="Jane")
  take_order()
  await asyncio.gather(staff1.working(), staff2.working())

if __name__ == "__main__":
  s = time.perf_counter()
  asyncio.run(main())
  elapsed = time.perf_counter() - s
  print(f"Orders completed in {elapsed:0.2f} seconds.")