import threading
import time

order_queue = []
def take_order():
   for i in range(3):
       order_queue.append(make_burger(i))

def make_burger(order_num):
   def making_burger():
       print(f"Preparing burger #{order_num}...")
       time.sleep(5)  # time for making the burger
       print(f"Burger made #{order_num}")
   return making_burger

def working():
     while len(order_queue) > 0:
         print(f"{threading.current_thread().name} is working...")
         task = order_queue.pop(0)
         task()
         print(f"{threading.current_thread().name} finish task...")

def main():
   take_order()
   staff1 = threading.Thread(target=working, name="John")
   staff1.start()
   staff2 = threading.Thread(target=working, name="Jane")
   staff2.start()
   staff1.join()
   staff2.join()

if __name__ == "__main__":
 s = time.perf_counter()
 main()
 elapsed = time.perf_counter() - s
 print(f"Orders completed in {elapsed:0.2f} seconds.")