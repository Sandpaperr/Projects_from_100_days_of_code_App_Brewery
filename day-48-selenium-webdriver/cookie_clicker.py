from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
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

    while time.time() - start_time < 1:
        cookie_to_click.click()

def upgrade():

    #store all the upgrades available
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div:not(.grayed):not(.amount)")
        
    #If I can still buy upgrades
    while upgrades:
        try:
            #get the greatest upgrade we can afford
            id_upgrade = upgrades[-1].get_attribute("id")
        
            print(f"Attempting to buy upgrade with ID: {id_upgrade}")

            # Click on the upgrade
            upgrade_to_buy = driver.find_element(By.ID, id_upgrade)
            upgrade_to_buy.click()
        except StaleElementReferenceException:
            print("Stale reference encountered. Skipping this upgrade.")
        except NoSuchElementException:
            print("No such element")
            for upgrade in upgrades:
                print(upgrade.text)

        try:
            #store all the upgrades available
            upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div:not(.grayed):not(.amount)")

        except NoSuchWindowException:
            upgrades = None
    else:
        print("No available upgrades at the moment.")
        upgrades = None


        

while True:
    cookie_click_5_seconds()
    upgrade()