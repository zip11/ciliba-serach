from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import os



#ciliba
def bctxt(wenzi):

#保存链接到txt
    file_object = open('xz.txt', 'a')
    all_the_text = wenzi+'\n'
    file_object.write(all_the_text)
    file_object.close( )

def hqcl(wz1,dk1):

#打开单页，提取链接
    driver.get(wz1)
    
    try:
        #等待2s，加载网页
        time.sleep(2)
    finally:

        html = driver.page_source

        doc = pq(html)
        #print(doc)
        items = doc('#mg-link')
        print(items)
        #链接的id名字，pyqu提取
        
        one=str(items)
        soup = BeautifulSoup(one,"html.parser")
        #a提取网址链接
        cll=soup.find('input')['value']
        print(cll)
    return cll;


def srwz():
#主页输入搜索词
    
    print('download www.ciliba.biz 2018-12-22 ')
    #driver.get("https://www.ciliba.org/")


#关闭弹出警告

    #search_element = driver.find_element_by_name('s') 
    #定位输入框的位子
    wz1 = input("wang zhi shu ru :")
    return wz1

def sysr(wz2):


    driver.get("https://www.ciliba.biz/s/"+wz2+".html")
    time.sleep(2)
    
    #关闭弹出警告
    alert = driver.switch_to_alert()
    alert.accept()

    time.sleep(2)
    #search_element.send_keys(wz1) 
    #输入搜索信息

    #button_element = driver.find_element_by_id('btnSearch') 
    #定位搜索按钮的位子
    time.sleep(1)
    #button_element.click() 
    #点击搜索按钮



def tqxz():


    #目录页提取单页网址
    
    try:
        
        element = WebDriverWait(driver,2).until(   #until 也属于WebDriverWait,代表一直等待,直到某元素可见，until_not与其相反，判断某个元素直到不存在
        EC.presence_of_element_located((By.ID, "wall"))  #presence_of_element_located主要判断页面元素kw在页面中存在。
        )
    finally:
        #提取目录页,下载页码地址
        html = driver.page_source
        #pyqu对象
        doc = pq(html)
        #print(doc)
        #下载网页标题id
        items = doc('.item-title') 
        print(type(items))
        #pyqu类型转字符串
        one = str(items)
        print(one[0:30])
        #bs4对象
        soup = BeautifulSoup(one,"html.parser")
        #a提取网址链接
        er=soup.find_all('a')
    return er;

#新建游览器对象
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)

wz3 = srwz()
#输入搜索词

driver = webdriver.Chrome(chrome_options=chrome_options)

sysr(wz3)
#提取下载页的磁力链接
san = tqxz()

os.remove('xz.txt')
#删除，文件

#提取list,单个元素,
zs1 = len(san)
print('link number ',zs1)
#网址数量
i = 1

for lj in san:

    #下载页链的网址
    wz=lj.get('href')
    print('webpage ',i,wz)
    
    #如果是第一页，关闭提示
    if i==1:
        cl1=hqcl(wz,True)
    else:
        cl1=hqcl(wz,False)
    
    #下载链接
    print('cili link ',cl1)
    #保存txt
    bctxt(cl1)
    i = i + 1
    print('shen yu link num',zs1-i+1,'\n')
driver.quit()
print('link end')
