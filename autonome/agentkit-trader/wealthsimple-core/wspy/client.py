from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import pickle
import time
import random
import threading
import json

def get_driver():
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--start-maximized")  # Optional: Start browser maximized
    # options.add_argument("--headless")  # Optional: Run in headless mode
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    # Download here https://googlechromelabs.github.io/chrome-for-testing/
    if sys.platform == "darwin":
        service = Service(executable_path=os.path.join(os.path.dirname(__file__), "chromedriver-mac-arm64/chromedriver"))  # Update path to chromedriver
    elif "win" in sys.platform and sys.platform != "darwin":
        service = Service(executable_path=os.path.join(os.path.dirname(__file__), "chromedriver-win64/chromedriver.exe"))
    elif "linux" in sys.platform:
        service = Service(executable_path=os.path.join(os.path.dirname(__file__), "chromedriver-linux64/chromedriver.exe"))

    driver = webdriver.Chrome(service=service, options=options)
    return driver

xpath_input_email = '/html/body/div[1]/ws-card-loading-indicator/div/div/div/div/ng-transclude/div/layout/div/div[2]/main/login-wizard/wizard/div/div/ng-transclude/form/ws-micro-app-loader/login-form/span/div/span/div/div/div[2]/div[1]/div[1]/div/div[1]/input'
xpath_input_password = '/html/body/div[1]/ws-card-loading-indicator/div/div/div/div/ng-transclude/div/layout/div/div[2]/main/login-wizard/wizard/div/div/ng-transclude/form/ws-micro-app-loader/login-form/span/div/span/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/input'
xpath_input_otp = '/html/body/div/ws-card-loading-indicator/div/div/div/div/ng-transclude/div/layout/div/div[2]/main/login-wizard/wizard/div/div/ng-transclude/form/login-two-factor-form/div/div/ws-micro-app-loader/two-factor-auth-details/span/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/input'
#selector_input_otp = '#input--20ea5f40-61ba-4b38-9e4a-af1b399df6d0'

xpath_crypto_price = '//*[@id="main"]/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/p/div/div[1]'
xpath_crypto_cent = '//*[@id="main"]/div/div/div[1]/div[3]/div/div[1]/div[1]/div/div/div/div/div[1]/p/div/div[1]/div/div[last()]'

changes_sometimes = '//*[@id="main"]/div/div/div[1]/div[HERE, 2 to 3]/div/div[1]/div[1]/div/div/div/div[1]/p/div/div[2]/div[last()]'
xpath_stock_price = '//*[@id="main"]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/p/div/div[2]'
xpath_stock_cent = '//*[@id="main"]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/p/div/div[2]/div[last()]'
# changes_sometime= '//*[@id="main"]/div/div/div[1]/div[HERE, 4 to 5]/div[2]/div/div/div/div[1]/div[1]/div/p[HERE, 2 to nothing]'
# xpath_stock_bid = '//*[@id="main"]/div/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[1]/div/p'
# xpath_stock_ask = '//*[@id="main"]/div/div/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div/p'

selector_stock_ask = '[data-qa="wstrade-info-item-Ask"]'
selector_stock_bid = '[data-qa="wstrade-info-item-Bid"]'
selector_stock_last = '[data-qa="wstrade-info-item-Last sale"]'

selector_menu_btn_activity = '[data-qa="menu-item-list-activity"]'
selector_menu_btn_move = '[data-qa="menu-item-list-move"]'

homepage_safe_buttons = [6,9,10,11,12,13,16,17,26,30]
xpath_buttons_on_homepage = '(//*/button)' # add [0], [1]... some index to select a specific button


class Client():
    def __init__(self,
                 url_login = "https://my.wealthsimple.com/app/login",
                 url_home = "https://my.wealthsimple.com/app/home"):
        self.url_login = url_login
        self.url_home = url_home
        self.driver = get_driver()
        self.windows = {}
        self.bearer_token = ""
        self.cookies = None
        self.login_status = "CREDS" # "BAD_CREDS", "OTP", "BAD_OTP", "OK"

    # ====================================================================================================
    # capture bearer token from network log
    # ====================================================================================================

    def scrape_bearer_token(self, duration=60, repeat=2):
        # default is to do it twice. during testing it nees twice to find the token
        # TODO is to use the refresh token somehow
        for i in range(repeat):
            # refreash to home screen
            self.driver.get(self.url_home)
            # and capture the bearer token
            start_time = time.time()
            print(f"Capturing network logs for {duration} seconds...")
            while time.time() - start_time < duration:
                logs = self.driver.get_log('performance')
                for entry in logs:
                    log = json.loads(entry['message'])['message']
                    if log['method'] == 'Network.requestWillBeSent':
                        request = log['params']['request']
                        if 'url' in request and request['url'].endswith('graphql'):
                            self.bearer_token = request['headers']['authorization']
                            if self.bearer_token == "":
                                print("Bearer token not found, trying again...")
                                continue
                            return
                time.sleep(1)
        return self.bearer_token
    
    
    # ====================================================================================================
    # Login
    # ====================================================================================================

    def open_main_window(self, url=None):
        url = self.url_home if None else self.url_login
        self.driver.get(url)
        # register teh current window handle as main
        main_window = self.driver.current_window_handle
        self.windows["main"] = main_window

    def login(self, email, password, duration=120, repeat=1):
        if "main" not in self.windows:
            self.open_main_window(url=self.url_login)
        for _ in range(repeat):
            start_time = time.time()
            self._login(email, password, duration=duration)
            # main purpose is to capture the bearer token
            print(f"Capturing network logs for {duration} seconds...")
            while time.time() - start_time < duration:
                logs = self.driver.get_log('performance')
                for entry in logs:
                    log = json.loads(entry['message'])['message']
                    if 'Network.response' in log['method']:
                        response = log['params']['response']
                        if 'url' in response and response['url'].endswith('token'):
                            if "access_token" in response:
                                # no need for otp, logged in
                                # update bearer token
                                self.bearer_token = response["access_token"]
                                self.login_status = "OK"
                                return self.login_status
                            elif "error" in response and "headers" in response:
                                response_headers = response['headers']
                                if "x-wealthsimple-otp" in response_headers and "required" in response_headers[ "X-Wealthsimple-Otp"]:
                                    self.login_status = "OTP"
                                    return self.login_status
                                else:
                                    self.login_status = "BAD_CREDS"
                                    return self.login_status
                time.sleep(1)
        self.login_status = "UNKNOWN,BAD_CREDS"
        return self.login_status
    
    def otp(self, otp, duration=120, repeat=1):
        for _ in range(repeat):
            start_time = time.time()
            self._login_otp(otp, duration=duration)
            # main purpose is to capture the bearer token
            print(f"Capturing network logs for {duration} seconds...")
            while time.time() - start_time < duration:
                logs = self.driver.get_log('performance')
                for entry in logs:
                    log = json.loads(entry['message'])['message']
                    if 'Network.response' in log['method']:
                        response = log['params']['response']
                        if 'url' in response and response['url'].endswith('token'):
                            if "access_token" in response:
                                # no need for otp, logged in
                                # update bearer token
                                self.bearer_token = response["access_token"]
                                self.login_status = "OK"
                                return self.login_status
                            elif "error" in response and "headers" in response:
                                response_headers = response['headers']
                                if "x-wealthsimple-otp" in response_headers and "required" in response_headers[ "X-Wealthsimple-Otp"]:
                                    self.login_status = "OTP"
                                    return self.login_status
                                else:
                                    self.login_status = "BAD_CREDS"
                                    return self.login_status
                time.sleep(1)
        self.login_status = "UNKNOWN,BAD_CREDS"
        return self.login_status

    # function to login
    def _login(self, email, password, duration=60):
        print("Nav to login url...")
        self.driver.get(self.url_login)
        print("Logging in...")
        # check if input email and password fields are present
        ready = False
        start_time = time.time()
        while not ready:
            if time.time() - start_time >= duration:
                return "TIMEOUT"
            try:
                # check if the email and password input fields are present
                email_input = self.driver.find_element(By.XPATH, xpath_input_email)
                password_input = self.driver.find_element(By.XPATH, xpath_input_password)
                ready = True
            except:
                print("Waiting for login page to load...")
                time.sleep(1)
        # Find the email input field
        email_input = self.driver.find_element(By.XPATH, xpath_input_email)
        email_input.send_keys(email)

        # Find the password input field
        password_input = self.driver.find_element(By.XPATH, xpath_input_password)
        password_input.send_keys(password)

        # Submit the login form (usually pressing Enter works)
        password_input.send_keys(Keys.RETURN)
        print("submitted login form")

    # function to enter otp
    def _login_otp(self, otp, duration=60):
        # check if input email and password fields are present
        ready = False
        start_time = time.time()
        while not ready:
            if time.time() - start_time >= duration:
                return "TIMEOUT"
            try:
                # check if the otp input fields are present
                otp_input = self.driver.find_element(By.XPATH, xpath_input_otp)
                ready = True
            except:
                print("Waiting for otp page to load...")
                time.sleep(1)
        # Find the email input field
        otp_input = self.driver.find_element(By.XPATH, xpath_input_otp)
        otp_input.send_keys(otp)

        # Submit the login form (usually pressing Enter works)
        otp_input.send_keys(Keys.RETURN)
        print("submitted otp form")

    # def login(self, email, password):
    #     # check if the cookies file exists
    #     # if not, login and save cookies
    #     if not os.path.exists("cookies.pkl"):
    #         print("No cookies found. May require 2FA...")
    #         self._login(email, password)
    #         # wait for user to enter 2FA
    #         input("Press Enter after you have entered 2FA")
    #         self.save_cookies()
    #     else:
    #         # Load cookies
    #         print("Loading cookies...")
    #         cookies = pickle.load(open("cookies.pkl", "rb"))
    #         for cookie in cookies:
    #             self.driver.add_cookie(cookie)
    #         # reload the page
    #         print("Reloading page...")
    #         self.driver.refresh()
    #         self._login(email, password)
    #         self.save_cookies()

    #     # wait until we get to the home page
    #     while self.driver.current_url != self.url_home:
    #         time.sleep(1)
    #     print("Logged in successfully")
    #     print("Getting token...")
    #     self.scrape_bearer_token()
    #     print("Network logs captured")



    # def save_cookies(self):
    #     # Save cookies
    #     print("Saving cookies...")
    #     self.cookies = self.driver.get_cookies()
    #     # pickle.dump(self.cookies, open("cookies.pkl", "wb"))
    #     print("Cookies saved")