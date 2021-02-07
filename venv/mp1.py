import multiprocessing
import time
def disp():
     for i in range(5):
        print("hi")
        time.sleep(2)

def show():
    for i in range(5):
        print("hello")
        time.sleep(2)

if __name__=='__main__':
    p=multiprocessing.Process(target=disp)
    q=multiprocessing.Process(target=show)
    p.start()
    time.sleep(0.5)
    p.join()
    q.start()