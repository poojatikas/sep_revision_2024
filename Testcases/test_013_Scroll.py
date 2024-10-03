import time

from selenium import webdriver


class Test_013_Scroll_By_mouse():

    def test_013_01_Scroll(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.bbc.com/")

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_013_scrollBy_pass.png")

        driver.execute_script("window.scrollBy(0,1000)")
        # driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_013_scrollby1_pass.png")

        driver.close()
        assert True
