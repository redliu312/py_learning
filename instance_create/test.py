from cached_property import cached_property
import time

class a:
    def __init__(self,message):
        self.message = message

    def b(self):

        print(self.message)

    @cached_property
    def c(self):
        import pdb;pdb.set_trace()
        print("c"+self.message)
        return time.time() 


if __name__=='__main__':

    aa = a("hello")
    aa.b()
    #aa.c()
