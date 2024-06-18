import pytest
@pytest.fixture(scope = "function")
def dbconnection():
    print("open db connection")

    yield
    print("close the db browser")
@pytest.mark.userfixture("dbconnection")
def test_createquery():
    print("table is created")

@pytest.mark.userfixture("dbconnection")
def test_createquery():
    print("table is deleted")

@pytest.mark.userfixture("dbconnection")
def test_createquery():
    print("table is selected")
