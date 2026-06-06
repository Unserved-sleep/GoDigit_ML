import threading
import time
import logging

num = 0
queue_lock = threading.Lock()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logging.basicConfig(level=logging.DEBUG,filename="thrd",filemode="w")


def increment():
    with queue_lock:
        global num
        temp = num
        time.sleep(0.001)
        num = temp + 1
    logger.info(f"increment {num}")

def decrement():
    with queue_lock:
        global num
        temp = num
        time.sleep(0.001)
        num = temp - 1
    logger.info(f"decrement {num}")

def main():
    threads = []

    logger.info("Starting thread")
    for _ in range(10):
        t = threading.Thread(target=increment)
        u = threading.Thread(target=decrement)
        threads.append(t)
        threads.append(u)
        t.start()
        u.start()

    for t in threads:
        t.join()
    print(num)
    logger.info("Ending thread")

if __name__ == "__main__":
    main()