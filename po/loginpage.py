#author="Simon song"
#coding:utf-8
#登录页面类
from base.bases import Base
class loginPage(Base):
    username_loc=("id","kw")
    password_loc=()
    submit_loc=("id","su")
    remember_loc=()
    def input_username(self,username):
        """
        输入用户名
        """
        self.send(self.username_loc,username)
    def input_password(self,password):
        """
        输入密码
        """
        self.send(self.password_loc,password)
    def submit_click(self):
        """
        点击登录按钮
        """
        self.click_loc(self.submit_loc)
    def gettile(self):
        """
        获取页面title
        """
        Title=self.driver.title
        return Title