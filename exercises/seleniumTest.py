from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://mmmphoto.github.io/Development-Portfolio/')
elems = browser.find_elements(By.TAG_NAME, "p")

aboutText = ''
for i in range(len(elems) - 1):
    aboutText += f'{aboutText}{elems[i].text} '
print(aboutText)

browser.close()
browser.quit()