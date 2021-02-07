from threading import Thread
from time import sleep

class ex(Thread):
    def run(self):
        for i in range(5):
            sleep(2)
            print("hi")

class ex1(Thread):
    def run(self):
        for i in range(5):
            sleep(2)
            print('hello')

x=ex()
x1=ex1()
x.start()
x.join()
x.setName('Thead-hi')
print(x.getName())
sleep(1)
x1.start()
print(x1.getName())

print(x.is_alive())



