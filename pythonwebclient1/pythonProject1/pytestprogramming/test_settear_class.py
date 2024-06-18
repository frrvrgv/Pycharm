class TestClass:
    def setup_class(cls):
        print("API connection is opened")
    def teardown_class(cls):
        print("API connection is closed")
    def setup_method(self,method):
        print("open browser")
    def teardown_method(self,method):
        print("browser is closed")
    def test_01(self):
        print("test 01 is executed")
    def test_02(self):
        print("test o2 is executed")
