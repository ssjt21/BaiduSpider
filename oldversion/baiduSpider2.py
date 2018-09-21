# -*- coding: utf-8 -*-

"""
@author:随时静听
@file: baiduSpider2.py
@time: 2018/09/21
@email:wang_di@topsec.com.cn
"""

from selenium import webdriver

import time
pages=10
keyword=u"inurl:?.asp学校"

url="https://www.baidu.com/"


def getUrls(driver):
    urls=[]
    current_window=driver.current_window_handle
    # print current_window
    # next_page_url

    for a in driver.find_elements_by_xpath("//div[@id='content_left']//div/h3/a"):
        a.click()

    all_windows=driver.window_handles
    print all_windows
    all_windows.remove(current_window)
    # for window in all_windows:
    #     if window!= current_window:
    #         driver.switch_to_window(window)
    #         urls.append(driver.current_url)
    #         print driver.current_url
    for window in all_windows:

        driver.switch_to_window(window)
        urls.append(driver.current_url)
        print driver.current_url

    print len(all_windows)
    #复原
    for window in all_windows[:]:
        driver.switch_to_window(window)
        driver.close()
    driver.switch_to_window(current_window)
    # driver.
    # time.sleep(20)
    return urls,driver

def doSearch(url,keyword,driver):
    # driver=webdriver.PhantomJS()

    driver.get(url)
    driver.find_element_by_id('kw').send_keys(keyword)
    driver.find_element_by_id('su').submit()
    # driver.f
    time.sleep(5)


    return driver

def toNextpage(driver):
    pages = driver.find_elements_by_xpath("//div[@id='page']//a")
    # print pages
    if pages:
        pages[-1].click()
    return  driver
def run():
    pages=11

    urls=[]
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver=doSearch(url,keyword,driver)

    # urls.extend( getUrls(driver))
    for i in range(pages+1):
        # driver=toNextpage(driver)

        url_lst,driver=getUrls(driver)
        urls.extend(url_lst)
        driver=toNextpage(driver)
        time.sleep(3)
    #
    # print len(urls)
    # except:
    #     print 123
    #     pass
    #     # driver.close()
run()
if __name__ == '__main__':
    pass