from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.olx.bg")
print(driver.title)

time.sleep(5)
cookie = driver.find_element("id", "onetrust-accept-btn-handler")
cookie.send_keys(Keys.RETURN)

time.sleep(5)

search = driver.find_element("id", "cityField")
search.send_keys("Варна")
search.send_keys(Keys.RETURN)
search.send_keys(Keys.RETURN)

send = driver.find_element("id", "submit-searchmain")
send.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()

