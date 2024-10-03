import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_016_screenshots():

    def test_016_ss(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@id="username"]').send_keys('student')

        driver.find_element(By.XPATH,'//input[@id="password"]').send_keys('Password123')

        driver.find_element(By.XPATH,'//button[@id="submit"]').click()

        if (driver.title=="Logged In Successfully | Practice Test Automation"):
            print('*************WELCOME TO ORANGEHRM HOME PAGE***********')

            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_016_hrm_screenshot_pass.png")
            time.sleep(1)

            print("*********LOGIN SUCESSFULLY*********")


            driver.find_element(By.XPATH,'//a[contains(text(),"Log out")]').click()

            driver.close()
            assert True

        else:

            driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_016_hrm_ss_fail.png")
            print("*************LOGIN FAILED************")
            driver.close()
            assert False



    def test_016_addition(self):

        a=10
        b=5
        add=a+b
        if(add==15):
            print("**********ADDITION SUCESFULLY******")
            print("ADDITION:",add)
            assert True
        else:
            print("************SORRY,ADDITION IS NOT POSSIBLE*******")
            assert False



# pytest -v -s -W "ignore" "Testcases/test_016_screenshots.py" --html="
# Report\report.html" --alluredir="D:\pythonProject1\pythonProject\pythonProject\pythonProject\Sep_2024_revision\allure-results"










