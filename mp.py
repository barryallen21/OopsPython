from multiprocessing import Process
def disp():
    print("welcome")

if __name__=='__main__':
    m=Process(target=disp)
    m.start()