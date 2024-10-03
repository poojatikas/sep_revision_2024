import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_011_drag_and_drop():

    def test_011_drag_drop(self):

        driver=webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demo.automationtesting.in/Static.html")

        action= ActionChains(driver)

        src=driver.find_element(By.XPATH,'(//img[@id="angular"])[1]')
        des=driver.find_element(By.XPATH,"//div[@id='droparea']")

        action.drag_and_drop(src,des).perform()
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_011_drag_drop_pass.png")
        image = pyautogui.screenshot()
        image.show()
        image.save("test_011_drag_drop_pass.png")

        driver.close()
        assert True




