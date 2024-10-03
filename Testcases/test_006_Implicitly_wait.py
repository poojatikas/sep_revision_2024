import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_006_Implicit_wait():

    def test_006_imp_wait(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(30)

        driver.get("https://www.google.co.in/")

        driver.find_element(By.XPATH,'//textarea[@aria-label="Search"]').send_keys('INTERNET SPEED TEST')

        driver.find_element(By.XPATH,'(//input[@value="Google Search"])[1]').click()

        driver.find_element(By.XPATH,'(//div[@class="lv7K9c"])[1]').click()
        time.sleep(25)

        Downloadspeed = driver.find_element(By.XPATH,'//div[@class="oyUhj"]').text
        print('\n*************INTERNET DOWNLOAD SPEED***********')
        print(Downloadspeed)

        Uploadspeed = driver.find_element(By.XPATH,'//div[@class="iD3Ij"]').text
        print('\n*************INTERNET UPLOAD SPEED*************')
        print(Uploadspeed)

        driver.save_screenshot('D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_006_imp_wait_pass.png')
        image = pyautogui.screenshot()
        image.show()
        image.save("test_006_imp_wait_pass.png")

        driver.close()
