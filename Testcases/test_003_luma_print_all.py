import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_003_luma_login():

    def test_003_login_printall(self):

        driver=webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com")

        driver.find_element(By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("aruna2@web.com")

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys('Aruna@001')

        driver.find_element(By.XPATH,'(//span[text()="Sign In"])[1]').click()

        if(driver.title=="Home Page"):
            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_003_luma_print_all_pass.png")
            print('*********LOGIN SUCESSFULLY********')
            image = pyautogui.screenshot()
            image.show()
            image.save("test_003_luma_print_all_pass.png")

            driver.find_element(By.XPATH,'(//button[@class="action switch"])[1]').click()

            driver.find_element(By.XPATH,'(//a[text()="My Account"])[1]').click()

            print('****** User DEtails******')
            text1=driver.find_element(By.XPATH,"//p[contains(text(),'Aruna Nimje')]").text
            print(text1)

            print('******User Address*******')
            text2=driver.find_element(By.XPATH,"//div[@class='box box-shipping-address']//address[contains(text(),'Aruna Nimje')]").text
            print(text2)

            driver.find_element(By.XPATH,"//div[@class='panel header']//button[@type='button']").click()
            time.sleep(1)

            driver.find_element(By.XPATH,'(//a[contains(text(),"Sign Out")] )[1]').click()
            time.sleep(1)

            assert True
            driver.close()
        else:
            driver.save_screenshot('D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_003_login_printall_fail.png')
            print('*********LOGIN UNSUCESSFULLY********')
            image = pyautogui.screenshot()
            image.show()
            image.save("test_003_login_printall_fail.png")
            assert False
            driver.close()
