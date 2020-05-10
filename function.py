

from selenium import webdriver
from browsermobproxy import Server
import time

class CheckDate:

    def __init__(self,url):
        self.url = url
        self.proxy = None
        self.driver = None
        self.server = None


    def chrome_proxy_driver(self):
        # 开启浏览器代理服务
        # self.server = Server()
        # self.server.start()
        # self.proxy = self.server.create_proxy()
        #
        # # 设置chrome驱动以proxy方式开启，若在linux系统执行时进行以下配置
        # chrome_options = webdriver.ChromeOptions() # 为驱动加入无界面配置
        # chrome_options.add_argument('--headless') # 不用打开图形界面
        # chrome_options.add_argument('--no-andbox') # 让chrome在root权限下执行
        # chrome_options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))

        self.driver = webdriver.Chrome("C:\\Users\\86186\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")


    def login(self):
        print("login")
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[text()='超级管理员登录']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@placeholder='用户名']").send_keys("大象云电")
        self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("888888")
        self.driver.find_element_by_xpath("//*[@type='submit']").click()

    # def access_modules(self):


    def run(self):
        self.chrome_proxy_driver()
        self.login()
        # self.driver.quit()

if __name__ == "__main__":
    cd = CheckDate("https://panel.dxyundian.com")
    cd.run()








