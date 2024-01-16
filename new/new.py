import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonWebsiteAddressAutoSubmit:
    def init(self):
        options = webdriver.ChromeOptions()  # Replace with your preferred browser
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)  # Set implicit wait for page elements

    def main(self):
        try:
            self.driver.get("https://www.amazon.in/a/addresses/add?ref=ya_address_book_add_post")

            login_page = LoginPage(self.driver)
            login_page.set_username("your_email@example.com")
            login_page.continueButtonClick()
            login_page.set_password("your_password")
            login_page.click_button()

            new_address_details = NewAddressDetails(self.driver)
            new_address_details.set_fullname("Your Full Name")
            # ... Fill in other address fields
            new_address_details.click_button()

            # Verification (optional)
            time.sleep(5)  # Wait for address addition
            self.driver.get("https://www.amazon.in/a/addresses")
            print("Address added successfully!")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.driver.quit()

class LoginPage:
    def init(self, driver):
        self.username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        self.password = driver.find_element(By.ID, "ap_password")
        self.button = driver.find_element(By.ID, "signInSubmit")
        self.continueButton = driver.find_element(By.ID, "continue")

    # ... (Methods for login actions)

class NewAddressDetails:
    def init(self, driver):
        # ... (Initialize WebElements)

    # ... (Methods for entering address details)

if name == "main":
    auto_submit = AmazonWebsiteAddressAutoSubmit()
    auto_submit.main()