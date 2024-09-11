import pytest
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

