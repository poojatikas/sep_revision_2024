import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Test_007_Explicit_wait():

    def test_007_Exp_wait(self):

        driver= webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.google.co.in/")

        driver.find_element(By.XPATH,'//textarea[@aria-label="Search"]').send_keys("Internet speed Test")

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()

        driver.find_element(By.XPATH,'(//div[@class="lv7K9c"])[1]').click()
        time.sleep(1)

        try:
            wait = WebDriverWait(driver,25,poll_frequency=0.5)

            wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[text()="TEST AGAIN"]')))

            Downloadspeed=driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text
            print('***********INTERNET DOWNLOAD SPEED*******')
            print(Downloadspeed)

            Uploadspeed=driver.find_element(By.XPATH,'(//div[@class="iD3Ij"])[1]').text
            print('*********INTERNET UPLOAD SPEED************')
            print(Uploadspeed)

            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_007_exp_wait_pass.png")
            driver.close()

        except:
            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_007_exp_wait_fail.png")
            driver.close()
