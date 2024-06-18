import pytest
pytest.mark.parametrize('input1, input2, exp_op',[
    (1,2,3)
    (0,0,0)
    (1,-1,0)
    ("hello", "world", "helloworld"),
])
def test_add(input1,input2,exp_op):
    assert input1 + input2 ==exp_op
