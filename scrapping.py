import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url=input('')
browser=webdriver.Chrome(
"C:/Users/Dell/Downloads/chromedriver.exe"
)
page=browser.get(url)
html=browser.page_source
#bs=BeautifulSoup(html,"html.parser")
#filename="data/links.html"


#bss=bs.prettify()

#with open(filename,"w") as f:
# for link in bs.find_all("p",p=True):
# print(link['p'])
# f.write(bss)

element = browser.find_elements_by_class_name('nologin')
filename="data/ques.yml"

with open(filename,"w") as f:
       for value in element:
            print(value.text)
            f.write(value.text)