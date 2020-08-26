from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import schedule


"""
26-08-2020

Open source
EDUCATIONAL purpose only
Developed by Sumukh Jadhav
"""

def glogin(browser, email, password):
    browser.get("https://accounts.google.com/login")
    time.sleep(2)

    webdriver.ActionChains(browser).send_keys(email).perform()
    time.sleep(1)
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(7)

    webdriver.ActionChains(browser).send_keys(password).perform()
    time.sleep(1)
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()
    time.sleep(10)

def meetlogin(browser, url, callDur):
    browser.get(url)
    time.sleep(5)

    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)

    webdriver.ActionChains(browser).send_keys(Keys.TAB * 6).perform() 
    webdriver.ActionChains(browser).send_keys(Keys.ENTER).perform()

    time.sleep(callDur * 60)  
    
    browser.close()

    
def main():
    
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--deny-permission-prompts ")
    
    browser = webdriver.Chrome(chrome_options=chrome_options)

    # Would not recommend using your primary account :)

    email = '----USERNAME-----'                    #Enter GMAIL here
    password = '--PASSWORD--'                      #Enter PASSWORD here
    url = '-----MEETING URL/LINK----'              #Enter Meeting URL here
    callDur = 30                                   #Enter how long you want the call to last (in MINUTES)
    glogin(browser, email, password)
    
    meetlogin(browser, url, callDur)

main()