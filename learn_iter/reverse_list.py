


class reverse_iter:

    def __init__(self,iterable):
        self.iterable = iterable
        self.cursor = 0
        self.n  = len(self.iterable)

    def  __iter__(self):
        '''
        return a iterable
        '''
        return self

    def __next__(self):
        '''
        __next__ in python3
        next in python2


        '''
        while self.cursor < self.n:
            value =  self.iterable[self.n-self.cursor-1]
            self.cursor += 1
            return  value

        raise StopIteration





def test_reverse_iter():
    test_list = [1,2,3,4]
    r_list = []
    for i in reverse_iter(test_list):
        r_list.append(i)
    assert r_list == [i for i in reversed(test_list)]
