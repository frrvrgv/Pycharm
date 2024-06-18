import pytest
def square(n):
    return n**2
pytest.mark.parametrize('input1,result',[
    (1,1),(2,4),(4,16),
])
def test_square(input1,result):
    assert square(input1) == result