from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return ts + '\t'


def start_browser():
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-pipe")
    return webdriver.Chrome(options=options)


def login(driver, user, password, ):
    print(timestamp() + 'Starting the browser...', )
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    product_label = driver.find_element(By.CSS_SELECTOR, "span[class='title']").text
    assert "Products" in product_label
    print(timestamp() + f'Login with username {user} and password {password} successfully.', )


def add_to_cart(driver, item_count):
    for i in range(item_count):
        element = f"a[id='item_{i}_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        count = driver.find_element(By.CSS_SELECTOR, "span[class='shopping_cart_badge']").text
        assert int(count) == (i + 1)
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name large_size']").text
        print(timestamp() + f"{product} added to shopping cart.", )
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + f"{item_count} items are all added to the shopping cart successfully.", )


def remove_from_cart(driver, item_count):
    for i in range(item_count):
        element = f"a[id='item_{i}_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        if i < N_ITEMS - 1:
            count = driver.find_element(By.CSS_SELECTOR, "span[class='shopping_cart_badge']").text
            assert int(count) == N_ITEMS - (i + 1)
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name large_size']").text
        print(timestamp() + f"{product} removed from the shopping cart.", )
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + f"{item_count} items are all removed from the shopping cart successfully.")


if __name__ == "__main__":
    N_ITEMS = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'

    xdriver = start_browser()
    login(xdriver, TEST_USERNAME, TEST_PASSWORD)
    add_to_cart(xdriver, N_ITEMS)
    remove_from_cart(xdriver, N_ITEMS)
    print(timestamp() + 'Selenium tests are all successfully completed!')
