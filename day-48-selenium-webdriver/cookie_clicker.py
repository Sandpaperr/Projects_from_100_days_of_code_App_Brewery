from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#whitout this line amazon detect the robot
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie_to_click = driver.find_element(By.ID, value="cookie")

def cookie_click_5_seconds():
    start_time = time.time()

    while time.time() - start_time < 5:
        cookie_to_click.click()

def upgrade():
    #store my money
    my_money = int(driver.find_element(By.ID, value='money').text)

    #store all the upgrades available
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div:not(.grayed)")
    print(upgrades)

    

    #TODO: fix bug, after first upgrade, it stops
    #If I can still buy upgrades
    while upgrades:
        #get the greatest upgrade we can afford
        id_upgrade = upgrades[-1].get_attribute("id")
        upgrade_to_buy = driver.find_element(By.ID, value=id_upgrade)
        upgrade_to_buy.click()

        upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div:not(.grayed)")


        

while True:
    cookie_click_5_seconds()
    upgrade()