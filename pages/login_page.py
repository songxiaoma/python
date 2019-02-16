from common.base import Base
class Login_page(Base):
    loc1=("id","username")
    loc2=("id","passwd")
    loc3=("xpath","/html/body/div[1]/div/div/div[2]/div[1]/form/fieldset[2]/div/section[1]/label/span")
    loc4=("xpath","//*[@id='form_button']")
    loc5=("xpath","/html/body/header/div[2]/div[4]/span")
    def input_user(self,text=""):
        self.sendele(self.loc1,text)
    def input_password(self,text=""):
        self.sendele(self.loc2,text)
    def remmber_psw(self):
        self.clickele(self.loc3)
    def click_login_button(self):
        self.clickele(self.loc4)
    def is_Text(self):
        p=self.is_text(self.loc5)
        return p
if __name__=="__main__":
    from selenium import webdriver
    from time import sleep
    driver=webdriver.Firefox()
    driver.get("http://g7s.huoyunren.com/#cf_truck_intellitrailer/v3/loadMonitor")
    login_page=Login_page(driver)
    login_page.input_user("VLtest")
    login_page.input_password("ht2A605")
    sleep(5)
    login_page.remmber_psw()
    sleep(5)
    login_page.click_login_button()

