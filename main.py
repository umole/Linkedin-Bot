import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, \
    ElementClickInterceptedException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3294713354&distance=25.0&f_AL="
           "true&geoId=105365761&keywords=python%20developer")
linkedin = driver.find_element(By.LINK_TEXT, "Sign in")
linkedin.click()

# signin to linkedin
time.sleep(2)
sign_in_email = driver.find_element(By.XPATH, '//*[@id="username"]')
sign_in_email.send_keys("ferdgm@yahoo.com")
sign_in_password = driver.find_element(By.XPATH, '//*[@id="password"]')
sign_in_password.send_keys("**********")
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.send_keys(Keys.ENTER)

# find each job posting and save them and also follow the companies
time.sleep(5)
job_listing = driver.find_elements(By.CSS_SELECTOR, "a.job-card-list__title")
for jobs in job_listing:
    print(jobs.text)
    jobs.click()
    time.sleep(5)
    save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    save.click()
    time.sleep(10)
    try:
        follow = driver.find_element(By.LINK_TEXT, 'Follow')
        follow.click()
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print("Unfortunately, couldn't follow!")
        pass

