import time
from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://dev.hellodoc.app/web/auth")
    time.sleep(3)
    driver.quit()