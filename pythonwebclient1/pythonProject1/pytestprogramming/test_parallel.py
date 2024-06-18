import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#testcase1
def testcase1():
    print("Testcase 1 is execute")
    print("Testcase 2 is execute")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("http://www.facebook.com/")

#testcase2
def testcase2():
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("http://www.google.com/")


#testcase3
def testcase3():
    print("Testcase 3 is execute")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("http://www.selenium.dev/")
