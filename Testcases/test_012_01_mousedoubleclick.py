import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_012_01_double_click():

    def test_012_01_doubleclick(self):

        driver= webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://artoftesting.com/samplesiteforselenium")

        double_click=driver.find_element(By.XPATH,'//button[@id="dblClkBtn"]')

        action = ActionChains(driver)

        action.double_click(double_click).perform()
        time.sleep(1)

        Msg1=Alert(driver).text
        print('\n',Msg1)

        Alert(driver).accept()
        time.sleep(1)

        driver.save_screenshot("D:\pythonProject1\pythonProject\pythonProject\pythonProject\Sep_2024_revision\Screenshots\\test_012_01_doubleclick_pass.png")
        image = pyautogui.screenshot()
        image.show()
        image.save("test_012_01_doubleclick_pass.png")

        driver.close()
        assert True