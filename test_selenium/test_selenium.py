import selenium
from selenium import webdriver


def test_selenium():
    a = webdriver.Chrome()
    a.get("https://www.baidu.com/")
