import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_002_lumalogin():

    def test_002_luma(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com")

        driver.find_element(By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys('aruna2@web.com')

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys('Aruna@001')

        driver.find_element(By.XPATH,'(//span[text()="Sign In"])[1]').click()
        time.sleep(1)

        if (driver.title=="Home Page"):
            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_002_luma_details_pass.png")
            print("**********Login Sucessfully*******")
            image = pyautogui.screenshot()
            image.show()
            image.save("test_002_luma_details_pass.png")

            print('***********Welcome Text********')
            text1=driver.find_element(By.XPATH,'(//span[@class="logged-in"])[1]').text
            print(text1)

            driver.find_element(By.XPATH,"//div[@class='panel header']//button[@type='button']").click()

            driver.find_element(By.XPATH,' (//a[contains(text(), "Sign Out")])[1]').click()
            assert True
            driver.close()

        else:
            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_002_luma_details_fail.png")
            print("*********Login Unsucessfully******")
            image = pyautogui.screenshot()
            image.show()
            image.save("test_002_luma_details_fail.png")

            assert False
            driver.close()

