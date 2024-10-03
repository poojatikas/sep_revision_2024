import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test_008_02_Facebook():

    def test_008_02_FB_Dropdown(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.facebook.com")

        driver.find_element(By.XPATH,'//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()

        driver.find_element(By.XPATH,'(//input[@name="firstname"])[1]').send_keys('Neha')

        driver.find_element(By.XPATH,'(//input[@name="lastname"])[1]').send_keys('More')

        driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys('7845261385')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@autocomplete="new-password"]').send_keys('Neha@111')
        time.sleep(1)

        Day=Select(driver.find_element(By.XPATH,'//select[@id="day"]'))
        Day.select_by_value('13')

        Month=Select(driver.find_element(By.XPATH,'//select[@id="month"]'))
        Month.select_by_index(8)

        Year = Select(driver.find_element(By.XPATH,'//select[@id="year"]'))
        Year.select_by_visible_text('2024')

        driver.find_element(By.XPATH,'//label[contains(text(),"Female")]').click()

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_008_02_fb_dd_pass.png")
        driver.close()






















