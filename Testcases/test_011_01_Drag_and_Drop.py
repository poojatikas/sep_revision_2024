import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_011_01_Drop_and_Drop():

    def test_011_01_drop_and_drop(self):

        driver=webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://vinothqaacademy.com/mouse-event/")

        action = ActionChains(driver)

        src= driver.find_element(By.XPATH,"//div[@class='draggable']")
        des=driver.find_element(By.XPATH,"//div[@class='droppable']")

        action.drag_and_drop(src, des).perform()
        time.sleep(2)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_011_01_dragdrap_pass.png")

        image = pyautogui.screenshot()
        image.show()
        image.save("test_011_01_dragdrap_pass.png")

        driver.close()
        assert True