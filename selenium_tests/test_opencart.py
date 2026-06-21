import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "http://localhost:8081"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_open_main_page(driver):
    driver.get(BASE_URL)
    time.sleep(2)
    assert "OpenCart" in driver.title or driver.current_url == BASE_URL + "/"

def test_logo_presence(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#logo img, .logo img, header img")))
    assert logo.is_displayed()

def test_navigation_menu(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav, .navbar, #menu, .menu")))
    assert menu.is_displayed()

def test_search_functionality(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "search")))
    search_input.send_keys("iPhone")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], .btn-search, #search button")
    search_button.click()
    time.sleep(2)
    assert "search" in driver.current_url or "route=product/search" in driver.current_url

def test_open_category(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    category_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktops")))
    category_link.click()
    time.sleep(2)
    assert "path=" in driver.current_url or "desktop" in driver.current_url.lower()

def test_open_product_card(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-thumb, .product-layout")))
    product.click()
    time.sleep(2)
    wait.until(EC.url_contains("product_id="))
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()

def test_add_to_cart(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-thumb")))
    product.click()
    time.sleep(2)
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "button-cart")))
    add_button.click()
    time.sleep(2)
    success_msg = driver.find_element(By.CSS_SELECTOR, ".alert-success, .alert, #alert")
    assert success_msg.is_displayed()

def test_open_cart(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart, .cart, [id*='cart']")))
    cart_icon.click()
    time.sleep(2)
    assert "checkout/cart" in driver.current_url or "cart" in driver.current_url.lower()

def test_open_login_page(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    my_account = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account")))
    my_account.click()
    time.sleep(1)
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_link.click()
    time.sleep(2)
    assert "route=account/login" in driver.current_url

def test_footer_presence(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    footer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer, .footer, #footer")))
    assert footer.is_displayed()