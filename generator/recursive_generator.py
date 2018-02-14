#! /bin/python3
from inspect import isgenerator

def iter_over(generators):
    for i in generators:
        if isgenerator(i):
            for j in iter_over(i):
                yield j
        else:
            yield i

def recursive_generator(lis):
    if lis:
        yield lis[0]
        try:
            yield from recursive_generator(lis[1:])
        except:
            yield

def recursive_generator2(lis):
    if lis:
        yield lis[0]
        try:
            yield recursive_generator2(lis[1:])
        except:
            yield
def recursive_generator3(lis):
    if lis:
        yield lis[0]
        try:
            for i in recursive_generator3(lis[1:]):
                yield i
        except:
            yield


def main():
    
    for i in recursive_generator([1,2,3,4,5]):
        print (i)
    for i in recursive_generator2([1,2,3,4,5]):
        print (i)
    for i in recursive_generator3([1,2,3,4,5]):
        print (i)
if __name__ == '__main__':
    main()

