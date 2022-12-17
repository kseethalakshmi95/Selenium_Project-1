from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

class Edit():
    def test_2(self):


        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(10)
    # for username testcase1
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(5)
        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(4)
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        pimmodule=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        time.sleep(4)
        Editbutton=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div").click()
        time.sleep(20)
        act=ActionChains(driver)
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='First Name']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

        firstname= driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Seetha")
        time.sleep(4)
        act2=ActionChains(driver)
        act2.click(driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

        middlename=driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("Lakshmi")
        act1=ActionChains(driver)
        act1.click(driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

        lastname=driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("K")
        driver.implicitly_wait(10)
        save=driver.find_element(By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]").click()
        time.sleep(9)






s=Edit()
s.test_2()


