#coding:utf-8
import unittest
from selenium import webdriver
from pages.login_page import Login_page
from time import sleep
class LoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.a=Login_page(cls.driver)
    def setUp(self):
        self.driver.get("http://g7s.huoyunren.com/#cf_truck_intellitrailer/v3/loadMonitor")
        self.driver.delete_all_cookies()
        self.driver.refresh()
    #def test01(self):
        #print("-------测试开始------")
        #self.a.input_user("Ltest")
        #self.a.input_password("ht2A605")
        #self.a.remmber_psw()
        #self.a.click_login_button()
        #w=self.a.is_Text()
        #self.assertEqual(w,"自助服务")
        #print("-------测试结束------")
    def test02(self):
        print("-------测试开始------")
        self.a.input_user("Ltest")
        self.a.input_password("ht2A605")
        sleep(5)
        self.a.click_login_button()
        w=self.a.is_Text()
        print(w)
        self.assertEqual(w,"自助服务")
        print("-------测试结束------")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




