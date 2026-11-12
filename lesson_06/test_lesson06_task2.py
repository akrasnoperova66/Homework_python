from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    #Откройте страницу https://gitflic.ru/.
    driver.get("https://gitflic.ru/")

    #Установите cookie пользователя 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "YzI1MTY4NWUtMzZhZi00NGE3LTkwMjEtOTI0MTRiZTE4MzEx",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    #Обновите страницу.
    driver.refresh()

    #Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/an4ely")

    #Сохраните текущий URL.
    url_user1 = driver.current_url

    #Разлогиньтесь (очистите куки).
    driver.delete_all_cookies()

    driver.refresh()

    #Установите cookie пользователя 2. NjA3ZTgxNjYtNThhZS00NzUxLWIyM2EtODAxNGEyODllOTJh
    driver.add_cookie({
        "name": "SESSION",
        "value": "NjA3ZTgxNjYtNThhZS00NzUxLWIyM2EtODAxNGEyODllOTJh",
        "domain": "gitflic.ru"
    })
    
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    #Обновите страницу.
    driver.refresh()

    #Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/id44981271")

    #Сохраните текущий URL.
    url_user2 = driver.current_url


    #Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2


    driver.quit()
