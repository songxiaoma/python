from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.poll=0.5
    def findelement(self,locator):#查找元素函数
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*locator))
        return element
    def clickele(self,locator):#点击函数
        ele=self.findelement(locator)
        ele.click()
    def sendele(self,locator,text):#输入函数
        ele=self.findelement(locator)
        ele.send_keys(text)
    def clearele(self,locator):#清除函数
        ele=self.findelement(locator)
        ele.claer()
    def is_element_exist(self,locator):
        try:
            self.findelement(locator)
            return True
        except:
            return False
    def is_text(self,locator):
        ele=self.findelement(locator).text
        return ele

