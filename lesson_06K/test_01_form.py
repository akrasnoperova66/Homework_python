from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_fill():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("data-types-submitted"))

    assert "alert-danger" in driver.find_element(By.ID, "zip-code").get_attribute("class")

    chek_field_id = [
        "first-name", "last-name", "address", "city", "country",
        "e-mail", "phone", "job-position", "company"
    ]

    for field in chek_field_id:
        assert "alert-success" in driver.find_element(By.ID, field).get_attribute("class")

    driver.quit



