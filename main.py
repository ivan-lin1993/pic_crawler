from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def download_img(url):
    res = requests.get(url)
    filename = url.split('/')[-1]
    img = open("pic/{}".format(filename),'wb')
    img.write(res.content)


# download_img('https://cdn.pixabay.com/photo/2018/05/03/23/51/nature-3372857__340.jpg')


driver = webdriver.Firefox()
driver.get('https://pixabay.com/zh/photos/?cat=nature')

last_height = driver.execute_script("return window.scrollY")
# print(last_height)
SCROLL_PAUSE_TIME = 0.5
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

