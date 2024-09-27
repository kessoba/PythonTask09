import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length,expected_area",[(2,4),(4,16),(5,25)])
def test_multiple_square_areas(side_length,expected_area):
    assert shapes.square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length,expected_perimeter",[(2,8),(4,16),(5,20)])
def test_multiple_perimeter(side_length,expected_perimeter):
    assert shapes.square(side_length).perimeter() == expected_perimeter