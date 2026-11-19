from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    user_name = wait.until(
        EC.presence_of_element_located((By.ID, "user-name")))
    user_name.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    add_card = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_card.click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    pocket = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Cart, 3 items']")))
    pocket.click()
    checkout = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout")))
    checkout.click()

    first_name = wait.until(
        EC.presence_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Анна")
    driver.find_element(By.ID, "last-name").send_keys("Красноперова")
    driver.find_element(By.ID, "postal-code").send_keys("617470")
    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue")))
    continue_button.click()


    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    driver.quit()

    assert "$58.29" in total 



