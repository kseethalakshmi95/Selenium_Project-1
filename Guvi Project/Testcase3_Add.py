from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select

class Add():
    def pim3(self):


        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(20)
    # for username testcase1
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")

        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")

        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

        pimmodule=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()

        Addbutton=driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()

        #now we are adding employee info
        firstname=driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Ishanth")

        middlename=driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("Vats")

        lastname=driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("L")

        Id=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").clear()


        Id = driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(1995)

        button1=driver.find_element(By.XPATH,"//button[.=' Save ']")
        button1.click()

        #filling personal details

        nickname=driver.find_element(By.XPATH,"//label[text()='Nickname']/following::div[1]/input")
        time.sleep(2)
        nickname.send_keys("Yadav")
        time.sleep(5)
        otherid=driver.find_element(By.XPATH,"//label[text()='Other Id']/following::input").send_keys("1992")

        licensenumber=driver.find_element(By.XPATH,"(//input)[8]").send_keys(128990)
        ssnumber=driver.find_element(By.XPATH,"(//input)[10]").send_keys(526)
        sinnum=driver.find_element(By.XPATH,"(//input)[11]").send_keys(789)
        nationality=driver.find_element(By.XPATH,"//label[text()='Nationality']/following::div[1]")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(nationality).click().perform()
        selecting_role=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Indian']")
        ActionChains(driver).move_to_element(selecting_role).click().perform()
        time.sleep(5)

        maritalstatus=driver.find_element(By.XPATH,"//label[text()='Marital Status']/following::div[1]")
        ActionChains(driver).move_to_element(maritalstatus).click().perform()
        status=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='Married']")
        ActionChains(driver).move_to_element(status).click().perform()
        time.sleep(3)

        dob=driver.find_element(By.XPATH,"(//input[@placeholder='yyyy-mm-dd'])[2]").send_keys("2021-03-02")
        driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()

        gender=driver.find_element(By.XPATH,"//label[normalize-space()='Male']").is_selected()
        print(gender)
        militryservice=driver.find_element(By.XPATH,"(//input)[15]").send_keys("2years")

        Save=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)
        bloodtype=driver.find_element(By.XPATH,"//label[text()='Blood Type']/following::div[1]")
        ActionChains(driver).move_to_element(bloodtype).click().perform()
        result=driver.find_element(By.XPATH,"//div[@role='option']/span[text()='A+']")
        ActionChains(driver).move_to_element(result).click().perform()
        time.sleep(10)
        save2=driver.find_element(By.XPATH,"//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']").click()

        time.sleep(4)








p1=Add()
p1.pim3()












