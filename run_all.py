import unittest
from common import HTMLTestRunner_cn
casePath=r"C:\Users\G7\PycharmProjects\GS\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)
reportPath=r"C:\Users\G7\PycharmProjects\GS\report\report"+".html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                     title="登录验证",
                                    description="描述")
runner.run(discover)
fp.close()