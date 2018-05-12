from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


SCROLL_PAUSE_TIME = 0.5
driver = webdriver.Firefox()
url = "https://pixabay.com/zh/photos/?cat=nature&pagi="



def download_img(imgurl):
    try:
        res = requests.get(imgurl)
        filename = imgurl.split('/')[-1]
        img = open("pic/{}".format(filename),'wb')
        img.write(res.content)
    except:
        pass

def load_page(page):
    last_height = driver.execute_script("return window.scrollY")
    print("load page")
    while True:
        # Scroll down
        driver.execute_script("window.scrollBy(0, screen.height);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return window.scrollY")
        print(last_height,new_height)
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    imglistdiv = soup.findAll("div", {"class": "item"})
    print(len(imglistdiv))

    for img in imglistdiv:
        imgurl = img.find('img')['src']
        print(imgurl)
        download_img(imgurl)

def main():
    page = 21
    while True:
        driver.get(url+ str(page))
        load_page(page)
        page += 1
        time.sleep(1)

if __name__ == '__main__':
    main()