from learn_it import yrange

def test_it():
    yii = yrange(0,5)

    res = 0
    for i in yii:
        res += i
    assert res  == (0+1+2+3+4)
