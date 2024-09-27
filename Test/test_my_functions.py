import pytest

import time
import  source.my_functions as my_functions

def test_add():
    result = my_functions.add(3, 6)
    assert result == 9

def test_add_strings():
    result=my_functions.add('i like ',"burgers")
    assert result =="i like burgers"


def test_divided():
    result=my_functions.divided(10,5)
    assert result==2

def test_divided_byZero():
    with pytest.raises(ValueError):
        my_functions.divided(10,0)

@pytest.mark.slow    
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(3, 6)
    assert result == 9

@pytest.mark.skip(reason="the feature is currently broken")
def test_Add():
    assert my_functions.add(1,2) == 3
@pytest.mark.xfail(reason="we know we cannot divided by zero")
def test_divide_zero_broken():
    my_functions.divided(4,0)


