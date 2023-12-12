import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://amazon.com")
        self.assertIn("Amazon", driver.title)
        elem = driver.find_element(By.NAME, "field-keywords")
        elem.send_keys("ritfit")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()