from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#whitout this line amazon detect the robot
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

#PRICE FINDER FROM AMAZON PRODUCT
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"the price is {price_whole.text}.{price_cents.text}")



#Python.org
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")

#things I can do with driver element

#get placeholder value
print (search_bar.get_attribute("placeholder"))

#get the tag name
print(search_bar.tag_name)

button = driver.find_element(By.ID, value="submit")
print(button.size)

#find by CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)


#If all the method to find an element fail
#use Xpath -> way to locate an element by path structure
link_end = driver.find_element(By.XPATH, value=r'//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
print(link_end.text)

#to close the single page browser
driver.close()
#close all tabs 
driver.quit()