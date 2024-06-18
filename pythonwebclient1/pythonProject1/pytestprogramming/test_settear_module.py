import pytest
def setup_module(module):
    print("DB connection is opened")
def teardown_module(module):
    print("DB connection is closed")
#testcase1
def testcase1():
    print("testcase 1 ise execute")

#testcase2
def testcase2():
    print("Testcase 2 is execute")

#testcase3
def testcase3():
    print("Testcase 3 is execute")