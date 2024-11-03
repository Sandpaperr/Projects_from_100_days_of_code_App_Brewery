import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
from dotenv import load_dotenv
import os


load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL_LINKEDIN")
MY_PASSWORD = os.getenv("MY_PASSWORD_LINKEDIN")

#Keep the Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

driver.get(r"https://www.linkedin.com/jobs/search/?currentJobId=4034296435&f_AL=true&geoId=102943586&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

redirected = True
while redirected:
    try:
        time.sleep(2)
        sign_in_button = driver.find_element(By.CSS_SELECTOR, value="button.sign-in-modal__outlet-btn.cursor-pointer.btn-md.btn-primary")
        sign_in_button.click()
        redirected = False
        
    except NoSuchElementException:
        time.sleep(15)
        driver.get(r"https://www.linkedin.com/jobs/search/?currentJobId=4034296435&f_AL=true&geoId=102943586&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
        redirected = True

time.sleep(5)
email_input = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
password_input = driver.find_element(By.ID, value="base-sign-in-modal_session_password")

#input email and password to sign in
email_input.send_keys(MY_EMAIL)
password_input.send_keys(MY_PASSWORD)
sign_in_button = driver.find_element(By.CSS_SELECTOR, value="button.btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width")
sign_in_button.click()

#get all the job available
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")


#Instead of applying, I will just save the job. So I can check it later
for job in all_listings:
    print(job.text)
    job.click()
    time.sleep(1)
    save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()

#TODO: edge cases
#TODO: actually apply
#TODO: handle various first page redirections
#TODO: make a list of multiple job search and run the code iterating through them 
