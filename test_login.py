#coding=utf-8
from appium import webdriver
import unittest
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '3.0.1'
desired_caps['deviceName'] = '127.0.0.1：62001'
desired_caps['appPackage'] = 'com.bs.finance'
desired_caps['appActivity'] = '.ui.common.WelcomeActivity'

#TestCase类，所有测试用例类继承的基本类
class LoginTest(unittest.TestCase):
    #setUp（）方法用于测试用例执行前的初始化工作。如测试用例中需要访问数据库，可以在setUp中建立数据库链接
    #并进行初始化。如测试用例需要启动Appium服务，则需要在该方法内启动Appium服务。
    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #tearDown（）方法用于测试用例执行之后的善后工作。如关闭数据库连接，退出应用。
    #无论这个方法写在哪里，都是最后才执行
    def tearDown(self):
        self.driver.quit()
    #具体的测试用例，必须要以test开头
    def test_start(self):

        self.driver.find_element_by_id("com.bs.finance:id/linear_item_0").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("android.widget.LinearLayout").click()

if __name__ == '__main__':
    #构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件
    #loadTestsFromTestCase（）根据给定的测试类，获取其中的所有测试方法，并返回一个测试套件
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    #unittest框架的TextTestRunner（）类，通过该类下面的run（）方法来运行suite所组装的测试用例，入参为suite测试套件
    unittest.TextTestRunner(verbosity=2).run(suite)
