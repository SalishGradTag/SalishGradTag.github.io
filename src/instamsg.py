from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

LOAD_TIME = 4 #seconds

username = 'gt_test_kermit'
f = open("pwd.txt", "r")
password = f.read()

send_to = ''
url = 'https://instagram.com/'
text = "Eat my shorts"

def path():
    global driver
    # starts a new chrome session 
    driver = webdriver.Chrome() # Add path if required

def url_name(url): 
  driver.get(url)
  # adjust sleep if you want
  time.sleep(4) 

def login(user, pwd):
    
    '''
    log_but = driver.find_element(By.XPATH, "//div[text()='Log in']")
    time.sleep(2)
    log_but.click()
    time.sleep(4)
    
    return;
    '''

    # finds the username box 
    usern = driver.find_element(By.NAME, "username")
    # sends the entered username 
    usern.send_keys(user)
 
    # finds the password box 
    passw = driver.find_element(By.NAME, "password")
 
    # sends the entered password 
    passw.send_keys(pwd)
     
    # press enter after sending password
    passw.send_keys(Keys.RETURN) 
    time.sleep(LOAD_TIME*2)
     
def send_message():
   
    # Find message button
    message = driver.find_element(By.XPATH, "//*[contains(text(), 'Message')]") 
    message.click()
    time.sleep(LOAD_TIME)

    try:
        notif = driver.find_element(By.XPATH, "//*[contains(text(), 'Not Now')]") 
        notif.click();
        print("Not now")
    except:
        print("Nothing")


    time.sleep(0.1)

    xpath = ""
    l = 'Eat my shorts Logan'
    message_area = driver.find_element(By.XPATH, "//div[@aria-label='Message']")
    message_area.click()
    message_area.click(); 
    message_area.send_keys(l);
    message_area.send_keys(Keys.RETURN) 
    
    time.sleep(1)

path()
time.sleep(1)
url_name(url)
login(username, password)
url_name(url + '')
send_message()
#chrome.close()