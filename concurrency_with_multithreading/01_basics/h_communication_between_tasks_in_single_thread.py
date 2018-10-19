# 在多线程环境下，每个线程都有自己的数据，一个线程使用自己的局部变量比使用全局变量要好。因为局部变量只有线程自己可见，不会影响其他线程，而全局便来那个的
# 的修改必须加锁

# 局部变量也有问题，不同任务在同一个线程中如何通信？

"""
def process_student(name):
    std = Student(name)
    # std是局部变量，若每个子任务都要用到他，因此都要传进去
    do_task_1(std)
    do_task_2(std)
    print("end")

def do_task_1(std):
    do_sub_task_1(std)
    do_sub_task_2(std)
    ...
"""

import threading

local_school = threading.local()


def process_thread(name):
    local_school.student = name
    do_task_1()
    do_task_2()

def do_task_1():
    print("hello:{} in threading:{}".format(local_school.student,threading.current_thread().name))

def do_task_2():
    print("bye bye {}".format(local_school.student))

t1 = threading.Thread(target = process_thread, args=('allen',), name = 'Thread-a')
t2 = threading.Thread(target = process_thread, args=('jack',), name = 'Thread-b')
t1.start()
t2.start()
t1.join()
t2.join()
print("end...")

