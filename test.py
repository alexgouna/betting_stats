import multiprocessing
import time

def tesst():
    print("sssss")
    time.sleep(1)
    print("end of sleep 1...")


p1 = multiprocessing.Process(target=tesst)
p2 = multiprocessing.Process(target=tesst)


p1.start()
p2.start()
