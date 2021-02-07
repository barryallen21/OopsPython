from multiprocessing import Process

def add(*a):
    print(a)
    print(type(a))

if __name__ == '__main__':

    p = Process(target=add,args=(2,34,45))
    p.start()