from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Test_004_Alert():

    def test_004_Simple_Alert(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

        driver.find_element(By.XPATH,'//input[@id="alertexamples"]').click()

        Simple_alert=Alert(driver).text
        print('\n',Simple_alert)

        Alert(driver).accept()
        text1=driver.find_element(By.XPATH,"//p[@id='alertexplanation']").text
        print('**********TEXT AFTER ACCEPTING ALERT********')
        print(text1)

        driver.close()
        assert True

    def test_004_confirm_Alert(self):

            driver=webdriver.Chrome()

            driver.maximize_window()

            driver.implicitly_wait(5)

            driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

            driver.find_element(By.XPATH,'//input[@id="confirmexample"]').click()

            confirmalert=Alert(driver).text
            print('\n',confirmalert)

            # Alert(driver).accept()
            # Confirm_accept=driver.find_element(By.XPATH,"//p[@id='confirmexplanation']").text
            print('**********TEXT AFTER ACCEPTING ACCEPTING ALERT*********')
            # print(Confirm_accept)

            Alert(driver).dismiss()
            Confirm_dismiss=driver.find_element(By.XPATH,"//p[@id='confirmexplanation']").text
            print('*********TEXT AFTER CONFIRM DISMISSING ALERT********')
            print(Confirm_dismiss)
            driver.close()
            assert True


    def test_004_Prompt_Alert(self):

        driver= webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

        driver.find_element(By.XPATH,'//input[@id="promptexample"]').click()

        prop_alert=Alert(driver).text
        print('\n',prop_alert)

        Alert(driver).send_keys("I LOVE YOU")

        Alert(driver).accept()
        promp_alert_accept=driver.find_element(By.XPATH,'//p[@id="promptexplanation"]').text
        print('***********TEXT AFTER ACCEPTING ACCEPTING ALERT********')
        print(promp_alert_accept)

        # Alert(driver).dismiss()
        # promp_alert_dismiss=driver.find_element(By.XPATH,'//p[@id="promptexplanation"]').text
        print('***********TEXT AFTER DISMISSING PROMPT ALERT*********')
        # print(promp_alert_dismiss)
        driver.close()
        assert True








