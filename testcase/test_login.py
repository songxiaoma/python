#author="Simon song"
#coding:utf-8
#登录页面测试用例
import unittest
from po.loginpage import loginPage
from selenium import webdriver
from base.bases import Base
from time import sleep
login_url="https://www.baidu.com"
class TestLogin(unittest.TestCase):
    """
    登录测试类
    """
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=loginPage(cls.driver)
    def setUp(self):
        self.driver.get(login_url)
    def test_01(self):
        self.login.input_username("selenium")#输入用户名
        #self.login.input_password(self,username)#输入密码
        self.login.submit_click()#点击登录
        sleep(3)
        t=self.login.gettile()
        self.assertTrue(t=="selenium_百度搜索")
    def test_02(self):
        self.login.input_username("selenium")#输入用户名
        #self.login.input_password(self,username)#输入密码
        self.login.submit_click()#点击登录
        sleep(3)
        t=self.login.gettile()
        self.assertTrue(t=="selenium2_百度搜索")









