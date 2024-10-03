import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_012_mouse_doubleclick():

    def test_012_double_click(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        action=ActionChains(driver)

        Double_click=driver.find_element(By.XPATH,'//button[@ondblclick="myFunction()"]')

        action.double_click(Double_click).perform()
        time.sleep(1)

        msg1=Alert(driver).text
        print('\n',msg1)
        time.sleep(1)

        Alert(driver).accept()
        time.sleep(1)

        driver.save_screenshot('D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_012_mouse_doubleclick_pass.png')
        time.sleep(1)

        driver.close()
        assert True