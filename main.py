from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os, time
my_secret = os.environ['googlepassword']
ready = False
conjnumber = 0

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://conjuguemos.com/auth/login")
#username = driver.find_element(By.NAME, 'identity')
#username.send_keys("ok")

main_page = driver.current_window_handle

#click the cookie accept button
bruhcookie = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
bruhcookie.click()

#click the sign in with google button
aight = driver.find_element(By.CLASS_NAME, "abcRioButtonContentWrapper")
aight.click()
sleep(2)

for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle

#switches from the conjuguemos window to the google login window
driver.switch_to.window(login_page)
#select the google window and input username & pass
amongus = driver.find_element(By.TAG_NAME, "input")
amongus.send_keys("25ct4645@medinabees.org" + Keys.ENTER)
sleep(5)
#amongus.send_keys(my_secret)

oof = input("Have you logged in yet?[type 'yes' when done]: \n")
if oof == "yes":
  driver.switch_to.window(main_page)
  oof2 = input("What number conjuguemos would you like to do?: \n")
  conjnumber = int(oof2)

if conjnumber > 0:
  ready = True


if ready == True:
  #bruh = driver.find_element(By.TAG_NAME, "body")
  #bruh.send_keys(Keys.CONTROL, "f")
  #webdriver.ActionChains(driver).send_keys(Keys.CONTROL, "f").perform()

  matched_elements = driver.find_elements(By.CLASS_NAME, "row-number")

  texts = []
for matched_element in matched_elements:
    text = matched_element.text
    texts.append(text)

#assign 
amog = texts[conjnumber - 1]
amogstripped = amog.strip("VC").strip()
print(amogstripped)