import pytest
def test_simple_assertion():
    assert 1+1 == 2
def test_equal_assertion():
    x=5
    y=5
    assert x==y
def test_not_equal_assertion():
    x=4
    y=9
    assert x!=y
def test_in_assertion():
    num=[1,2,3,4,5,6]
    assert 3 in num
def test_not_in_assertion():
    fruits=["apple","banana","cherry"]
    assert "orange" not in fruits
def test_identity_assertion():
    a=[1,2,3]
    b=a
    assert a is b