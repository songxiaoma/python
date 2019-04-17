#author="Simon song"
#coding:utf-8
#Base基类-封装基本方法
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=30
        self.poll=0.5
    def findelement(self,loctor):#查找元素
        element=WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x:x.find_element(*loctor))
        r1=element.is_displayed()
        if r1==True:
            print("元素是显示的")
        else:
            print("元素是隐藏的")
        return element
    def send(self,loctor,text):#输入方法
        ele=self.findelement(loctor)
        ele.send_keys(text)
    def click_loc(self,loctor):#点击
        ele=self.findelement(loctor)
        ele.click()
    def isselect(self,loctor):#判断元素是否被选中
        ele=self.findelement(loctor)
        r=ele.is_selected
        return r
    def elementexsit(self,loctor):#判断元素是否存在
        try:
            self.findelement(loctor)
            return ("元素存在")
        except:
            return ("元素不存在")
    def titleexsit(self,text):#判断跳转页面是否正确,返回类型为bool
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.title_is( text))
            return element
        except:
            return False
    def elementtext(self,loctor,_text):#判断元素的文本信息,返回类型为bool
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(loctor, _text))
            return element
        except:
            return False
    def mouse_to_element(self,loctor):#移动鼠标
        ele=self.findelement(loctor)
        ActionChains(self.driver).move_to_element(ele).perform()
    def is_alert(self):#判断是否有弹窗
        try:
            element=WebDriverWait(self.driver,self.timeout,self.poll).until(EC.alert_is_present())
            return element
        except:
            return False
if __name__=="__main__":
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.select import Select
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    shishi=Base(driver)
    o=shishi.titleexsit("百度一下，你就知道")
    print(o)
    loc1=("link text","设置")
    r=shishi.elementtext(loc1,"设置")
    print(r)
    shishi.mouse_to_element(loc1)
    #ele1=shishi.findelement(loc1)
    #ActionChains(driver).move_to_element(ele1).perform()
    loc2=("link text","搜索设置")
    ele2=shishi.click(loc2)
    #loc3=("id","nr")
    #ele3=shishi.findelement(loc3)
    #Select(ele3).select_by_index(1)
    sleep(3)
    driver.quit()



