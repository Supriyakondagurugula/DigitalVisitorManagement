from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_visitor_registration():

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/")

    driver.find_element(By.NAME, "name").send_keys("Supriya")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "email").send_keys("supriya@gmail.com")
    driver.find_element(By.NAME, "person").send_keys("Manager")
    driver.find_element(By.NAME, "purpose").send_keys("Meeting")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    time.sleep(2)

    assert "Visitor Registered Successfully" in driver.page_source

    driver.quit()