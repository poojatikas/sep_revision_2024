import time

from selenium import webdriver

class Test_013_01_scroll_By_mouse():

    def test_013_mousescrollby(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://ed.ted.com/?utm_term=ted%20ed&utm_campaign=TED-Ed+site&utm_source=adwords&utm_medium=ppc&hsa_acc=7777130675&hsa_cam=18739292599&hsa_grp=151439764548&hsa_ad=631444589734&hsa_src=g&hsa_tgt=kwd-296155107571&hsa_kw=ted%20ed&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwxsm3BhDrARIsAMtVz6O8hI-lJIwThcqbdly9xoiHpTVh8uSHhjZ8lcKcijGFYvD6JCIEplMaAk-pEALw_wcB")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_013_01_beforescrollby_pass.png")

        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(1)

        driver.save_screenshot("D:\\pythonProject1\\pythonProject\\pythonProject\\pythonProject\\Sep_2024_revision\\Screenshots\\test_013_01_afterscrollby_pass.png")
        driver.close()
        assert True