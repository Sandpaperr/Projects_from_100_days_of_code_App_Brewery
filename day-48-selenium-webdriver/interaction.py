from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#whitout this line amazon detect the robot
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)


#Trying methods for interacting with a website
# #get hold of number of articles form wikipedia and click on the link
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# n_of_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# #n_of_articles.click()
# print(n_of_articles.text)

# #another way to click on link
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# #all_portals.click()


# # write and search in search bar
# search_bar = driver.find_element(By.NAME, value='search')

# #send keys. send enter -> same method for all special characters

# search_bar.send_keys("Python", Keys.ENTER)


#Sign online form

driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

name_field = driver.find_element(By.NAME, value="fName")
surname_field = driver.find_element(By.NAME, value="lName")
email_field = driver.find_element(By.NAME, value="email")

name_field.send_keys("test")
surname_field.send_keys("testttttt")
email_field.send_keys("test_test@gmail.com")

submit = driver.find_element(By.CLASS_NAME, value="btn")

submit.click()


#to close the single page browser
driver.close()
#close all tabs 
driver.quit()