import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_001_luma():

    def test_001_lumalogin(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com")

        driver.find_element(By.XPATH,"//div[@class='panel header']//a[normalize-space()='Create an Account']").click()

        driver.find_element(By.XPATH,'//input[@id="firstname"]').send_keys('Aruna')

        driver.find_element(By.XPATH,'//input[@id="lastname"]').send_keys('Nimje')

        driver.find_element(By.XPATH,'//input[@name="email"]').send_keys('aruna2@web.com')

        driver.find_element(By.XPATH,'(//input[@name="password"])[1]').send_keys('Aruna@001')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@title="Confirm Password"]').send_keys('Aruna@001')
        time.sleep(1)

        driver.find_element(By.XPATH,'//button[@title="Create an Account"]').click()
        time.sleep(1)

        if (driver.title == "My Account"):

            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_001_luma_pass.png");
            print("\n**********REGISTRATION SUCCESSFUL**********")
            image = pyautogui.screenshot()
            image.show()
            image.save("test_001_luma_pass.png")
            assert True
            driver.close()

        else:

            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_001_luma_fail.png");
            print("\n**********REGISTRATION UNSUCCESSFUL**********")
            image = pyautogui.screenshot()
            image.show()
            image.save("test_001_luma_fail.png")

            assert False
            driver.close()



