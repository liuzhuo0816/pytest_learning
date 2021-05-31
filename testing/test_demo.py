from time import sleep

from selenium import webdriver


webd = webdriver.Chrome()
webd.get("http://www.baidu.com")
sleep(3)
webd.find_element_by_xpath('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div').click()
sleep(3)
webd.close()

