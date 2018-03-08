from .learn_it import yrange

def test_it():
    yii = yrange(0,5)

    res = 0
    for i in yii:
        res += i
    assert res  == (0+1+2+3+4)


def test_for_equal():
    
    def  _ops():
        iterable = iter(yrange(0,5))
        res = []
        while True:
            item = next(iterable) 
            if item != StopIteration:
                res.append(item)
            else:
                break
        return res
    
    res = _ops()
    assert res == [i for i in range(5)]

        


