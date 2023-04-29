import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreditCardPaymentTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://devnoscope.luko.eu/my-account/")
        self.driver.maximize_window()

        # Log in
        log_in_email = self.driver.find_element(By.CLASS_NAME, "Lukomp-LkInput-🅿️")
        log_in_email.send_keys("qa-user@getluko.com")
        cookies_agree_close = self.driver.find_element(By.ID, "didomi-notice-agree-button")
        cookies_agree_close.click()
        log_in_password = self.driver.find_element(By.CSS_SELECTOR, "input#lukid-1[type='password']")
        log_in_password.click()
        log_in_password.send_keys("Faxs9YH5$yR#Rsag")
        sign_in = self.driver.find_element(By.CSS_SELECTOR,
                                           "#app > div > main > section > div > div.body-right > form > div.wrapper.wrapper--is-inline.wrapper--has-margin-top > button > span")
        sign_in.click()

    def tearDown(self):
        self.driver.quit()

    def test_SUCCESSFULL_credit_card_payment(self):
        # Navigate to payment methods and add credit card
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#side-menu-nav > ul > li:nth-child(5) > a > p"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Lukomp-LkButton-👄"))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))).click()

        # Fill in credit card details
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="stripe-card-number-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "cardnumber"))).send_keys("4242424242424242")
        self.driver.switch_to.default_content()

        wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="stripe-card-expiry-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "exp-date"))).send_keys("12/34")
        self.driver.switch_to.default_content()

        wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="stripe-card-cvc-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "cvc"))).send_keys("567")
        self.driver.switch_to.default_content()

        consent_agreement = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div/div[3]/div')
        consent_agreement.click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/button').click()
        # Assert that the card added successful
        success_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "body > div.Lukomp-LkPopin-👩‍🦱 > div > div > div.flex-col.flex-gap-12 > header > h1"))
        )
        self.assertEqual(success_message.text, "Success")

    def test_UNSUCCESSFULL_credit_card_payment(self):
        # Navigate to payment methods and add credit card
        payment_methods_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#side-menu-nav > ul > li:nth-child(5) > a > p")))
        payment_methods_field.click()
        add_payment_methods = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Lukomp-LkButton-👄")))
        add_payment_methods.click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/button[2]'))).click()

        # Fill in credit card details
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '//*[@id="stripe-card-number-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "cardnumber"))).send_keys("42424242424242")
        self.driver.switch_to.default_content()

        wait.until(
            EC.frame_to_be_available_and_switch_to_it(
                (By.XPATH, '//*[@id="stripe-card-expiry-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "exp-date"))).send_keys("12/34")
        self.driver.switch_to.default_content()

        wait.until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="stripe-card-cvc-element"]/div/iframe')))
        wait.until(EC.visibility_of_element_located((By.NAME, "cvc"))).send_keys("567")
        self.driver.switch_to.default_content()

        consent_agreement = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/div/div[3]/div')
        consent_agreement.click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/form/button').click()
        # Assert that the card can be added
        message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#card-cardNumber > p")))
        self.assertEqual(message.text, "Your card number is incomplete.")
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CreditCardPaymentTest('test_SUCCESSFULL_credit_card_payment'))
    suite.addTest(CreditCardPaymentTest('test_UNSUCCESSFULL_credit_card_payment'))

    unittest.TextTestRunner().run(suite)
