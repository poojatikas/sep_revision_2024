import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_DropDown():

    def test_008_DD(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.careinsurance.com/rhicl/proposalcp/renew/index-care")

        driver.find_element(By.XPATH,'//input[@id="policynumber"]').send_keys('12345695')

        driver.find_element(By.XPATH,'//input[@placeholder="DOB"]').click()
        time.sleep(1)

        Month =Select(driver.find_element(By.XPATH,'//select[@aria-label="Select month"]'))
        Month.select_by_index(8)
        time.sleep(1)

        Year = Select(driver.find_element(By.XPATH,'//select[@aria-label="Select year"]'))
        Year.select_by_value('2024')
        time.sleep(1)

        driver.find_element(By.XPATH,'//a[@data-date="13"]').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//input[@placeholder="Contact Number"]').send_keys('1234567891')
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_008_DD_pass.png")

        driver.close()





        #
        #
        #
