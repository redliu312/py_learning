import dis
import threading
"""
from  https://opensource.com/article/17/4/grok-gil
"""
n = 0
lst = [i for i in range(5)]
def foo():
    global n
    n += 1

def bar():

    lst.sort()


dis.dis(foo)
dis.dis(bar)
def share():
    threads= []
    for i in range(100):
        t = threading.Thread(target=foo)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(n)

if __name__ =="__main__":
    share()

