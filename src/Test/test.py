import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys 
import os 
from datetime import datetime

class GoogleTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        prefs = {
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("start-maximized")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_google_homepage(self):
        self.driver.get("https://www.google.com/")
        self.assertIn("Google", self.driver.title, "La página no es Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"..\reporthtmlrunner"))