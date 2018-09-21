# -*- coding: utf-8 -*-

"""
@author:随时静听
@file: baiduSpider2.py
@time: 2018/09/21
@email:wang_di@topsec.com.cn
"""

from selenium import webdriver

import time

#抓取多少页
pages=10
#搜索的关键字
keyword=u"inurl:?.asp学校"

#百度搜索URL地址
url="https://www.baidu.com/"

#获取页面的有效地址
def getUrls(driver):
    urls=[]
    #获取当前窗口
    current_window=driver.current_window_handle
    #百度跳转地址
    for a in driver.find_elements_by_xpath("//div[@id='content_left']//div/h3/a"):
        a.click()#点击进行跳转
    #获取打开的所有窗口，一会要将打开的窗口关闭，防止耗用电脑性能
    all_windows=driver.window_handles
    #所有窗口包含打开的搜索页面，不能将手搜页面关闭，所以将搜索页面剔除
    all_windows.remove(current_window)
    #对打开的页面进行关闭操作，这里一定要先关闭，再切换窗口，当前的driver是最后一个打开页面的窗口
    #因此如果先关闭的话容易导致出错，自行switchs 切换窗口已经销毁
    for window in all_windows:

        driver.switch_to_window(window)
        urls.append(driver.current_url)#统计获取到的URL
        print "[-] "+driver.current_url #打印下当前的URL

    print "[-] The number of pages parsed to URL is :"+str(len(all_windows))#打印页面获取了多少URL
    #复原
    #执行 其实这里可以和上面的循环一起处理
    for window in all_windows[:]:
        driver.switch_to_window(window)
        driver.close()
    #重新切换到搜索页面的窗口
    driver.switch_to_window(current_window)
    #返回抓取的URL和切换后的web对象
    return urls,driver

#执行搜索动作，并将改变状态后的web对象返回
def doSearch(url,keyword,driver):

    driver.get(url)
    driver.find_element_by_id('kw').send_keys(keyword)
    driver.find_element_by_id('su').submit()
    time.sleep(3)

    return driver

#执行点击下一页操作
def toNextpage(driver):
    pages = driver.find_elements_by_xpath("//div[@id='page']//a")
    if pages:
        pages[-1].click()
    return  driver

# 获取传递的参数:
def getargs():
    import sys
    usage='''
    Usage: BaiduSpider  keywords  [nums] [filename]
            keywords:   your Search keywords 
            nums:       default value is 6,seach max pages
            filename:   result saved file name，default value is result.txt
    
    '''
    if len(sys.argv)<2:
        print usage
        exit()
    else:
        try:
            keywords= sys.argv[1]
            if len(sys.argv)==2:
                # keywords= sys.argv[1] if sys.argv[1] else ""
                nums= 6
                filename="result.txt"
                return (keywords,nums,filename)
            if len(sys.argv)==3:
                nums= int(sys.argv[2])
                filename = "result.txt"
                return (keywords, nums, filename)
            if len(sys.argv)==4:
                nums = int(sys.argv[2])
                filename=sys.argv[3]
                return (keywords, nums, filename)
        except:
            print "[!] Parameter error !"
            print usage
            exit()

def saveData(urls,filename):
    if urls:
        with open(filename,'w') as f:
            for url in urls:
                f.write(url+'\n')

    print "[-] The urls total num is:"+str(len(urls))
    print "[-] The spider urls save as file:"+filename


#运行
def run():
    # pages=11
    #
    # urls=[]
    # driver = webdriver.Chrome()
    keyword,pages,filename=getargs()
    print "[-] Keywords:"+keyword
    print "[-] nums:"+str(pages)
    print "[-] save file name:"+filename


    urls=[]
    try:
        driver = webdriver.PhantomJS()
        driver.implicitly_wait(6)
        driver=doSearch(url,keyword,driver)

        for i in range(pages+1):
            print "[-] Page data loading: "+str(i+1)
            url_lst,driver=getUrls(driver)
            urls.extend(url_lst)
            driver=toNextpage(driver)
            time.sleep(2)
        saveData(urls,filename)
    except Exception as e:
        print "[!] There seems to be a mistake! The error message is as follows: "
        print "--"*6+"Error Message Info"+"--"*6
        print e
        print "--" * 6 + "Error Message  Info END" + "--" * 6
    finally:
        #关闭浏览器
        driver.quit()

if __name__ == '__main__':
    run()
    pass

