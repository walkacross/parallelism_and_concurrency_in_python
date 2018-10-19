import time
import datetime
import threading


shared_var = {}

#子线程待执行的代码
def loop():
    print("thread {} is to run,at {}".format(threading.current_thread().name, datetime.datetime.now()))
    n = 0
    while n < 5:
        n = n + 1
        print("thread {} is running, at n: {}".format(threading.current_thread().name, n))
        shared_var[str(n)] = n
        time.sleep(1)
    print("thread {} ended, at {}".format(threading.current_thread().name, datetime.datetime.now()))


print("thread {} is running at {}".format(threading.current_thread().name, datetime.datetime.now()))
t = threading.Thread(target=loop, name="LoopThread")
t.setDaemon(False)  # default is False
t.start()
print("thread {}, current shared_var : {}".format(threading.current_thread().name, shared_var))
time.sleep(1)
print("thread {}, current shared_var : {}".format(threading.current_thread().name, shared_var))
time.sleep(3)
print("thread {}, current shared_var : {}".format(threading.current_thread().name, shared_var))
print("thread {} ended at {}".format(threading.current_thread().name, datetime.datetime.now()))
