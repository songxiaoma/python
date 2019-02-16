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
    def is_element_exist(self):
        try:
            self.findelement(locator)
            return True
        except:
            return False

if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get("http://g7s.ucenter.huoyunren.com/login.html?referer=http%3A//g7s.huoyunren.com/%23cf_truck_intellitrailer/v3/loadMonitor")
    zentao=Base(driver)
    loc1=("id","username")
    loc2=("id","passwd")
    loc3=("id","form_button")
    zentao.sendele(loc1,"VLtest")
    zentao.sendele(loc2,"ht2A605")
    zentao.clickele(loc3)
