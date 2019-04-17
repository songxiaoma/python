
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
from public import HTMLTestRunner
from email.mime.text import MIMEText
import unittest
import time
import os,shutil
def send_mail(file_new):
	f=open(file_new,"rb")
	mail_body = f.read()
	f.close()
	msg=MIMEText(mail_body,"html","utf-8")
	msg["Subject"]=Header("自动化测试报告","utf-8")
	smtp=smtplib.SMTP()
	smtp.connect("smtp.126.com")
	smtp.login("song349877148@126.com","msj19921103")
	smtp.sendmail("song349877148@126.com","songxiaozhe@g7.com.cn",msg.as_string())
	smtp.quit()
	print("email has send out")
def new_report(testreport):
	lists=os.listdir(testreport)
	lists.sort(key=lambda fn:os.path.getatime(testreport + "\\" + "fn"))
	file_new=os.path.join(testreport,lists[-1])
	print(file_new)
	return file_new
if __name__ == "__main__":
	test_dir=r"C:\Users\songxiaozhe\PycharmProjects\lianxi\testcase"
	test_report=r"C:\Users\songxiaozhe\PycharmProjects\report"
	discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern="test*.py")
	print(discover)
	now=time.strftime("%Y-%m-%d_%H_%M_%S")
	reportPath=test_report+"_"+ now+ ".html"
	fp=open(reportPath,"wb")
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                     title="测试报告",
                                    description="用例执行情况")
	runner.run(discover)
	fp.close()
	print("好")
	new_report=new_report(test_report)
	print("的")
	send_mail(new_report)