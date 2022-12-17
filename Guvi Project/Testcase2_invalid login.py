from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class OrangeDemo():
    def test_1(self):


        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
    # for username testcase1
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")
        pwd = driver.find_element(By.NAME, "password").send_keys("invalid password")
        time.sleep(4)
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        widget=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div/div[2]")
        if widget.is_displayed():
            print("The user is logged in successfully")
        else:
            print("Login failed")
        driver.close()

s=OrangeDemo()
s.test_1()


