import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_09_Mouseover():

    def test_009_Over(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://stqatools.com/demo/MouseHover.php")

        action = ActionChains(driver)

        dropdown=driver.find_element(By.XPATH,'//button[@class="dropbtn"]')

        action.move_to_element(dropdown).perform()
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_09_mouseover_pass.png")
        image=pyautogui.screenshot()
        image.show()
        image.save("test_09_mouseover_pass.png")
        driver.find_element(By.XPATH,'(//a[@type="button"])[3]').click()

        Link3=(driver.find_element(By.XPATH,'//div[@class="modal-content"]')).text
        # print('*******Text after Over*******')
        print(Link3)
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_009_over_pass.png")
        image = pyautogui.screenshot()
        image.show()
        image.save("test_009_over_pass.png")
        driver.close()
        assert True







