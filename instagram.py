from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
from pyvirtualdisplay import Display

class Instagram():
    def __init__(self, user, passwrd):
        
        display = Display(visible=0, size=(800, 600))
        display.start()
        
        mobile_emulation = {

            "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

        chrome_options = Options()
        options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options = chrome_options)
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

        # login
        sleep(2)
        password = self.driver.find_element_by_name("password")
        username = self.driver.find_elements_by_name('username')[0]

        print(username.text)
        username.send_keys(user)
        password.send_keys(passwrd)
        password.send_keys(Keys.ENTER)

        # save password popup
        try:
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button').click()
        except: pass
        # add to homescreen popup
        try:
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Cancel')]").click()
        except: pass


    def upload(self, caption, name):
        # find the upload button
        sleep(1)

        upload = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        upload.click()
        sleep(1.5)

        pyautogui.hotkey('ctrl', 'f')
        sleep(2)
        pyautogui.write(name)
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        next_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        sleep(1.5)
        # caption
        caption_field = self.driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
        caption_field.send_keys(caption)
        # share button
        share_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
        sleep(10)

        # turn on notification popup
        try: self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        except: pass
