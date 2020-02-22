from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from credentials import *
from time import sleep
import autoit

def uploadimg(caption, path):
    mobile_emulation = {

        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options)

    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

    sleep(2)
    password = driver.find_element_by_name("password")
    username = driver.find_elements_by_name('username')[0]

    print(username.text)
    username.send_keys(user)
    password.send_keys(passwrd)
    password.send_keys(Keys.ENTER)
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
    except: pass
    try:
        sleep(1)
        driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
    except: pass
    sleep(1)
    upload = driver.find_element_by_xpath("//div[@role='menuitem']")
    upload.click()
    sleep(1.5)

    autoit.win_active("Open")

    sleep(1.5)
    autoit.control_send("Open","Edit1", path.replace('/','\\'))
    sleep(1.5)
    autoit.control_send("Open","Edit1","{ENTER}")

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)

    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
# F:/instagram bot/Unexpected/q8a12rvpdfi41.jpg
    sleep(10)
    driver.close()
# sleep(3)
# print(autoit.win_active("Open"))
# autoit.control_click("Open", "ToolbarWindow323", )
# sleep(1)
# autoit.control_set_text("Open", "ToolbarWindow323", "F:\\instagram bot\\Unexpected")
# sleep(1)
# autoit.control_send("Open", "ToolbarWindow323", "{ENTER}")
