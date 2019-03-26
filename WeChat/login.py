import json
import time

from selenium import webdriver



chrome_option = webdriver.ChromeOptions()


def login_sogou(myurl):
    # 模拟登录
    driver = webdriver.Chrome()
    driver.get(myurl)
    time.sleep(30)


    cookies = driver.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)

    # 测试cookie
    # with open("cookies.txt", "r") as fp:
    #     cookies = json.load(fp)
    #     for cookie in cookies:
    #         # cookie.pop('domain')  # 如果报domain无效的错误
    #         driver.add_cookie(cookie)
    #
    # driver.get('https://weixin.sogou.com/weixin?oq=&query=%E4%BF%9D%E9%99%A9&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=1&_sug_=n&type=2&sst0=1551405515524&page=1&ie=utf8&p=40040108&dp=1&w=01015002&dr=1')
    # time.sleep(20)

