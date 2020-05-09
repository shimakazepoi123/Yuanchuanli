from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import time

# 获取url，并通过原创力的ifram框架进入抓取图片（前提是可完整预览）
def read_url():
    url2 = 'https://max.book118.com/html/2020/0508/7045055050002133.shtm'
    aid = url2.split('/')[-1].replace('.shtm','')
    url = 'https://max.book118.com/index.php?g=Home&m=NewView&a=index&aid='+str(aid)+'&v=2020050802'
    return url


def download():
    a = read_url()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(a)
    
    # 通过点击使未加载图片链接加载出来
    click = driver.find_element_by_xpath('//*[@id="newView"]/div[1]/div/a[5]')
    page = driver.find_element_by_class_name('page-counts').get_attribute('innerHTML')
    page = page.split('/')[-1].lstrip()
    for i in range(int(page)):
        click.click()
        time.sleep(2)
        
    # 抓取网站源代码
    source = driver.page_source
    source1 = BeautifulSoup(source,'lxml')
    source2 = source1.select('.webpreview-item img')
    for i in range(len(source2)):
        source3 = source2[i].get('src')
        url2 = os.path.join('https:'+str(source3))
        r = requests.get(url2)
        if r.status_code == 200:
            open(str(i)+'.png', 'wb').write(r.content)


if __name__ == '__main__':
    download()
