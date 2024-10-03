import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Test_009_mouseover():

    def test_009_mouseover_Action(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys('vtiger')

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()

        driver.find_element(By.XPATH,'(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click()
        time.sleep(1)

        action = ActionChains(driver)

        solution_tab = driver.find_element(By.XPATH,"//body/nav[@class='navbar navbar-expand-lg p-0 py-3']/div[@id='s-zoom']/div[@id='navbarCollapse']/div[@class='custom-display-none-nav']/ul[@class='navbar-nav align-items-center']/li[5]/a[1]")
        action.move_to_element(solution_tab).perform()
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_009_mouseover_pass.png")
        image = pyautogui.screenshot()
        image.show()
        image.save("test_009_mouseover_pass.png")
        driver.find_element(By.XPATH,"//div[@class='col-4 p-lg-5']//a[@class='list-link'][normalize-space()='IT & Technology']").click()

        text1=driver.find_element(By.XPATH,'//span[@class="display-3 font-weight-bold"]').text
        print('\n',text1)

        driver.close()




































    


