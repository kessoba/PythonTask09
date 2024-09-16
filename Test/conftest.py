import pytest
import source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.rectangle(10,20)

@pytest.fixture
def weird_rectangle():
    return shapes.rectangle(5,6)