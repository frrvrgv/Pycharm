import pytest
#testcase1
@pytest.mark.sanity
def testcase1():
    print("Testcase 1 is execute")
#testcase2
@pytest.mark.regression
def testcase2():
    print("Testcase 2 is execute")
#testcase3
@pytest.mark.sanity
def testcase3():
    print("Testcase 3 is execute")
#testcase4
@pytest.mark.regression
def testcase4():
    print("Testcase 4 is execute")
#testcase5
@pytest.mark.sanity
def login():
    print("Testcase 5 is execute")

