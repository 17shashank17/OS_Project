from threading import Thread
from threading import Lock
import time

resource = time.strftime("%c")
lock = Lock()
counter = 0

class WriterA(Thread):
  def run(self):
    while True:
        global lock
        global resource
        global counter
        if counter == 0:
            lock.acquire()
            counter == -4
            resource = time.strftime("%c")
            print(resource)
            print ("Writer A acquired the lock and the message is: %s. " %resource)
            counter = 0
            lock.release()
            time.sleep(5)

class WriterB(Thread):
	def run(self):
		while True:
			global lock
			global resource
			global counter
			if counter == 0:
				lock.acquire()
				counter == -5
				resource = resource[::-1]
                
                #print(resource)
				print ("WriterB acquired the lock and the message is: %s. " %resource)
				counter = 0
				lock.release()
				time.sleep(5)

class Reader(Thread):
        def run(self):
            while True:
                global resource
                global counter
                if counter >= 0:
                    counter = 1
                    print ("Reader acquired the resource and the message is: %s" %resource)
                    counter -= 1
                    time.sleep(5)
                              

writerA = WriterA()
writerB = WriterB()
reader1 = Reader()
reader2 = Reader()
reader3 = Reader()

writerA.start()
writerB.start()
reader1.start()
reader2.start()
reader3.start()