import threading
import time

def make_burger(order_num):
   print(f"Preparing burger #{order_num}...")
   time.sleep(5) # time for making the burger
   print(f"Burger made #{order_num}")

def main():
   order_queue = []
   for i in range(3):
       task = threading.Thread(target=make_burger, args=(i,))
       order_queue.append(task)
       task.start()

   for task in order_queue:
       task.join()

if __name__ == "__main__":
   s = time.perf_counter()
   main()
   elapsed = time.perf_counter() - s
   print(f"Orders completed in {elapsed:0.2f} seconds.")