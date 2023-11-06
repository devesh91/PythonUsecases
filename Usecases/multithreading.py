from multiprocessing import current_process
from threading import current_thread,Thread
import time

sleep=10

def io_bound(sleep):



    print(f"Starting the thread")

    time.sleep(sleep)
    print("thread executed")

if __name__=="__main__":
    start_time = time.time()
    t1=Thread(target=io_bound,args=(sleep,))
    t2=Thread(target=io_bound,args=(sleep,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    end_time=time.time()
    print(f"total executed time {end_time-start_time}")
