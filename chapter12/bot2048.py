from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
game = browser.find_element(By.TAG_NAME, 'html')
for i in range(500):
    game.send_keys(random.choice((Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT)))
    time.sleep(1)

