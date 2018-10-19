import os

print("Process id {} start...".format(os.getpid()))

# here:
# 之后的代码会运行两次：因为操作系统自动的把当前进程(称为父进程)复制一份(称为子进程)，然后分别在父进程和子进程中各自执行
pid = os.fork()
if pid ==0:
    print("I am a child process {} and my parent process is {}".format(os.getpid(), os.getppid()))
else:
    print("I {} just created a child process {}".format(os.getpid(), pid))

print("end...")
