import pytest
@pytest.fixture
def square(request):
    return request.param * 2
#use indirect parametrization to pass arguments to the fixture
@pytest.mark.parametrize("square", [1,2,3], indirect=True)
def test_square(square):
    assert square in [2,4,6]