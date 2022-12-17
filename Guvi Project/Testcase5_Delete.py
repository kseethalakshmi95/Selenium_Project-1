from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Delete():
    def test_2(self):


        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
    # for username testcase1
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")

        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")

        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

        pimmodule=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()

        delete_element=driver.find_element(By.XPATH,"(//button[@type='button'])[40]")
        delete_element.click()
        time.sleep(5)
        yes=driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()
        time.sleep(10)

S1=Delete()
S1.test_2()