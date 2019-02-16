# coding=utf-8

import unittest
import time
import os
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common import HTMLTestRunner_cn
import smtplib
from email.mime.text import MIMEText
def send_mail(new_report):
    smtpserver="smtp.126.com"
    user="song349877148@126.com"
    password="msj19921103"
    sender="song349877148@126.com"
    receiver="songxiaozhe@g7.com.cn"
    subject="测试"

    #获取报告文件：'related'43行
    f = open(new_report,'rb')
    body_main = f.read()
    msg = MIMEMultipart()
    # 邮件标题
    msg["Subject"]=Header(subject,"utf-8")
    msg['From'] = "song349877148@126.com"
    msg['To'] = "songxiaozhe@g7.com.cn"
    #邮件内容
    text = MIMEText(body_main,'html','utf-8')
    msg.attach(text)

    #发送附件
    att = MIMEApplication(open(reportPath, 'rb').read())
    # att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', "report.html"))
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(user,password)
    smtp.sendmail(sender,receiver,msg.as_string())


if __name__=='__main__':
    print ('=====AutoTest Start======')
    #1.执行测试用例，生成最新的测试用例
    #指定测试用例为当前文件夹下的test_case目录
    #如果用/可以不用r
    casePath=r"C:\Users\G7\PycharmProjects\GS\case"
    rule="test*.py"
    discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
    print(discover)
    reportPath=r"C:\Users\G7\PycharmProjects\GS\report"+"report.html"
    fp=open(reportPath,"wb")
    runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                     title="登录验证",
                                    description="描述")
    runner.run(discover)
    fp.close()


    #3.发送邮件，发送最新测试报告html
    send_mail(reportPath)
    print ('=====AutoTest Over======')
