from multiprocessing import current_process, Process

import time

def cpu_bound():
    print("execution started")
    n=200000000

    while n>0:

        n-=1

if __name__=="__main__":
    start= time.time()
    # cpu_bound()
    # cpu_bound()
    p1=Process(target=cpu_bound)
    p2 = Process(target=cpu_bound)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end= time.time()

    print(f"total execution time {end-start}")
