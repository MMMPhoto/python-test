from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd-ebook/dp/B07VSXS4NK/')
elems = browser.find_elements(By.CSS_SELECTOR, '#kindle-price')

price = elems[0].text

print(price)

browser.close()
browser.quit()