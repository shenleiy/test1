import os
from multiprocessing import Process


def run(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(50):
        p = Process(target=run, args=(str(i),))
        print('Process will start.')
        p.start()
    p.join()
    print('Process end')
