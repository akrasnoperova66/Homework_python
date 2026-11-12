from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # 3. Дождитесь появления текста "Hello World!"
    hello_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/full_screen.png")


    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_element.is_displayed()
    assert hello_element.text == "Hello World!"

    driver.quit()
