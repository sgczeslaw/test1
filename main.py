import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from selenium.webdriver.common.by import By
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
driver = uc.Chrome(options=options, version_main=103)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)
driver.get("https://bitminerfarms.com/8059886255149546")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section[1]/div/div[1]/a").click()
time.sleep(2)


xd = False
time.sleep(4)
frime = driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[1]/div[5]/div/iframe")
driver.switch_to.frame(frime)
timez = int(time.time())+300
while xd == False:
    time.sleep(1)
    print(driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]").get_attribute("aria-checked"))
    if(timez<int(time.time())):
        cockz
    if(driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]").get_attribute("aria-checked")=="false"):
        xd = False
    else:
        xd = True
driver.switch_to.default_content()

emailrepl = "".join(random.sample(username_for, long_username))+"@cldkid.com"
usenrame = "".join(random.sample(username_for, long_username))
passwd = "".join(random.sample(username_for, long_username))


time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[1]/div[1]/input").send_keys(emailrepl) # email
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[1]/div[2]/input").send_keys(usenrame) # username
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[1]/div[3]/input").send_keys(passwd) #pass 
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[1]/div[4]/input").send_keys(passwd) # pass
time.sleep(1.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[2]/div[1]/input").click() # click
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/section/div/div/form/button").click() # button
