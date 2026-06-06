import threading
import time

num = 0

def increment():
    global num
    temp = num
    time.sleep(0.001)
    num = temp + 1

def decrement():
    global num
    temp = num
    time.sleep(0.001)
    num = temp - 1

def main():
    threads = []

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

if __name__ == "__main__":
    main()