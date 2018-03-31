

def stop_a_generator():

    for i in range(10):
        yield i
        if i == 5:
            yield None
            return



for i  in stop_a_generator():
    print (i)
