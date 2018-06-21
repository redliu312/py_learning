from retrytool import *

iii = 0

def some_func():
    global iii
    iii += 1
    print("hello")
    assert iii == 2
    print (iii)
    iii += 1

def test_retry():
    retry_some(some_func)
    print(iii)
    assert iii == 3

