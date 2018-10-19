import os
import time
import datetime
import multiprocessing

# code to be executaed by sub_procee
def run_proc(name):
    print("child process {} start, at {}".format(os.getpid(), datetime.datetime.now()))
    for i in range(5):
        print("Process {}: hello {}, at {}".format(os.getpid(), name, datetime.datetime.now()))
        time.sleep(1)
    print("child process end")

def main(name):
    print("parent process {} start, at {}".format(os.getpid(), datetime.datetime.now()))
    for i in range(5):
        print("Process {}: hello {}, at {}".format(os.getpid(),name, datetime.datetime.now()))
        time.sleep(1)
    print("parent process end")

if __name__ == "__main__":
    print("Parent process {} start, at {}".format(os.getpid(), datetime.datetime.now()))

    p = multiprocessing.Process(target=run_proc, args=('test',))
    p.start()

    main('allen')
    print("end....")


