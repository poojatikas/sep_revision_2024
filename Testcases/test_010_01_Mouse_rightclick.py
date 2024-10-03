import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_10_01_MouseRight_Click():

    def test_10_01_Right_Click(self):

        driver= webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://vinothqaacademy.com/mouse-event/")

        action = ActionChains(driver)

        right_click=driver.find_element(By.XPATH,'//button[@id="rightclick"]')

        action.context_click(right_click).perform()
        time.sleep(1)

        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_10_01_Rightclick_pass.png")
        image = pyautogui.screenshot()
        image.show()
        image.save("test_10_01_Rightclick_pass.png")

        text1=driver.find_element(By.XPATH,'//div[@id="myDiv"]').text
        print('*********Text After Right Click******')
        print(text1)

        driver.close()
        assert True







