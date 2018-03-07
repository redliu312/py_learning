class yrange:
    def __init__(self,*args):
        if len(args)>3 or len(args)==0:
            raise Exception
        if len(args) == 2:
            self.start = args[0]
            self.end = args[1]
        else :
            self.start = 0
            self.end =args[0]
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            res = self.start
            self.start +=1
            return res
        else:
            return StopIteration
 






















