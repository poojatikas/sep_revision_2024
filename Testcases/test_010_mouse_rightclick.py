import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

class Test_010_Rightclick():

    def test_010_Rightclick_action(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        action = ActionChains(driver)

        Right_click=driver.find_element(By.XPATH,'//span[text()="right click me"]')
        action.context_click(Right_click).perform()

        driver.save_screenshot('D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_010_rightclick_pass.png')
        image = pyautogui.screenshot()
        image.show()
        image.save("test_010_rightclick_pass.png")
        driver.find_element(By.XPATH,'//span[text()="Edit"]').click()

        text1=Alert(driver).text
        print('\n',text1)

        Alert(driver).accept()
        driver.close()