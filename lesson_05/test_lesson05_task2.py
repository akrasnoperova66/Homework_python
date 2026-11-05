from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.find_element(By.NAME, "custname").send_keys("Анна")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    assert "https://httpbin.qa-territory.online/forms/post" != driver.current_url


    driver.quit()
    