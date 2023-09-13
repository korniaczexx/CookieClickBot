import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 60 * 5
start = time.time()
last_purchase_time = start

while time.time() < timeout:
    elements = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store div b")
    text_elements = [ element.text for element in elements ]
    if (time.time() - last_purchase_time < 5):
        my_money = driver.find_element(By.ID, "money").text
        my_money = int(my_money.replace(",", " ").strip())
        for i in reversed(range(len(text_elements))):
            if i > 0:
                needed_money = int(text_elements[ i - 1 ].split("-")[ 1 ].replace(",", "").strip())
                if needed_money < my_money:
                    elements[ i - 1 ].click()
    cookie.click()
    last_purchase_time = time.time()

driver.quit()
