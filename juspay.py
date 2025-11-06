from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def automate_amazon():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()

    try:
        # ✅ 1. Open Amazon
        driver.get("https://www.amazon.in")
        time.sleep(3)

        # ✅ 2. Open login page
        driver.find_element(By.ID, "nav-link-accountList").click()
        time.sleep(3)

        # ✅ 3. Enter Email
        driver.find_element(By.ID, "ap_email_login").send_keys("kalyanbrahmam644@gmail.com")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # ✅ 4. Enter Password
        driver.find_element(By.ID, "ap_password").send_keys("Kalyan@012")
        driver.find_element(By.ID, "signInSubmit").click()
        time.sleep(5)

        # ✅ 5. Search for Product
        search = driver.find_element(By.ID, "twotabsearchtextbox")
        search.send_keys("headphones")
        search.send_keys(Keys.ENTER)
        time.sleep(5)

        # ✅ 6. Scroll the page (Amazon loads dynamic results)
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)

        # ✅ 7. Click First Product in Results
        # first_product = driver.find_element(
        #     By.XPATH, "(//div[@data-component-type='s-search-result'])[1]//h2/a"
        # )
        # first_product.click()
        # time.sleep(5)
        #
        # # ✅ Switch to product tab
        # driver.switch_to.window(driver.window_handles[1])

        # ✅ 8. Click Add to Cart
        try:
            add_cart_btn = driver.find_element(By.ID, "a-autoid-3-announce")
            add_cart_btn.click()
            print("✅ Added to Cart")
            time.sleep(5)
        except:
            print("❌ Add to Cart button not found")


        # ✅ 6. Scroll the page upwards (Amazon loads dynamic results)
        driver.execute_script("window.scrollBy(0, -600);")
        time.sleep(3)
    finally:
        time.sleep(5)

        cart_span = driver.find_element(By.XPATH,
                                        "/html/body/div[1]/header/div[1]/div[1]/div[3]/div/a[2]/div[1]/span[2]")
        cart_span.click()
        time.sleep(10)

        proceed_to_checkout=driver.find_element(By.NAME,"proceedToRetailCheckout")
        proceed_to_checkout.click()
        time.sleep(5)

if __name__ == "__main__":
    automate_amazon()
