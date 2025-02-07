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
import base64
import requests

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
        self.safe_webactivity_buttons = homepage_safe_buttons

        '''
        class MyStrategy(Strategy):
            
            client: Client
             
            def run():
                given new data
                emit buy and sell orders using the client

            def get_statsistics()
                cash - free money
                holdings:
                    lots:
                        shares
                        price_per_share                    
                        $ - some money are meant to be shorts
                could be too complex... maybe just have 

                net deposits vs net worth (max drawdown, max profit)
                equity vs cash split (exposure to risk, utilization rate)
                SMA ROI (avg roi over last 30days)

                <the task triplet> strategy, user, market (def as sybmol, time period)
                - read up the secret vault -- offline to learn
                - validation of operators: assume a good strategy has reproducable returns, drawdowns, and exposure given the underlying market condition
                                            overall the returns drawdowns and exposure are predictable(?)


            free to define everything else as it is convenient to the strategy
                - maybe positions are good because you by sell depending on each position (pinescript style)
                    profitability makes sense here, cuz you can talk about per position
                - maybe you work with orders and mix symbols together and just care about the final p&l (ws/tws style)  
                    time to double, ROI vs time/compared to asap buy & hold asset is good.


            positions = {
                "AAPL": {
                    "positions": [
                        {
                            "buy_order": "order-189b089d-68e9-4064-97f8-b8ddfe288fd4",
                            "buy_status": "filled",
                            "buy_size": 100,
                            "buy_price": 231,
                            "sell_order": None,
                            "sell_status": "pending"
                            "sell_size": None,
                            "sell_price": None
                        }, ..],
                }, ..
            }

            closed_positions = {
                "AAPL": {
                    "positions": [
                        {
                            "buy_order": "order-189b089d-68e9-4064-97f8-b8ddfe288fd4",
                            "buy_status": "filled",
                            "buy_size": 100,
                            "buy_price": 231,
                            "sell_order": "order-189b089d-68e9-4064-97f8-b8ddfe288fd4",
                            "sell_status": "filled"
                            "sell_price": 231,
                            "sell_size": 100
                        }, ..],
                    "cumulative_profit": 0,
                    "max_exposure": 0,
                    "current_exposure": 0,
                    "max_drawdown": 0,
                }, ..
        }
        '''
        positions = {}

    # ====================================================================================================
    # capture bearer token from network log
    # ====================================================================================================

    def scrape_bearer_token(self, duration=60, repeat=2):
        # default is to do it twice. during testing it nees twice to find the token
        # TODO is to use the refresh token somehow
        for i in range(repeat):
            # refreash to home screen
            self.driver.switch_to.window(self.windows['main'])
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

    def login(self, email, password, duration=30, repeat=1):
        if "main" not in self.windows:
            self.open_main_window(url=self.url_login)
        for _ in range(repeat):
            start_time = time.time()
            self._login(email, password, duration=duration)
            # main purpose is to capture the bearer token
            print(f"Capturing network logs for {duration} seconds...")
            while time.time() - start_time < duration:
                logs = self.driver.get_log('performance')
                print(f"Found {len(logs)} logs...")
                for entry in logs:
                    log = json.loads(entry['message'])['message']
                    if 'Network.responseReceived' in log['method'] and "params" in log and 'response' in log['params']:
                        response = log['params']['response']
                        if 'url' in response and response['url'].endswith('token'):
                            print(f"Network log: {json.dumps(log,indent=4)}")
                            try:
                                response_body = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
                                if response_body['base64Encoded']:
                                    response_body['body'] = base64.b64decode(response_body['body']).decode('UTF-8')                               
                                response_body = json.loads(response_body['body'])
                            except Exception:
                                response_body = {}
                            print(f"Body: {json.dumps(response_body, indent=4)}")
                            print("="*80)
                            if "access_token" in response_body:
                                # no need for otp, logged in
                                # update bearer token
                                self.bearer_token = response_body["access_token"]
                                self.login_status = "OK"
                                return self.login_status
                            elif "error" in response_body and "headers" in response:
                                response_headers = response['headers']
                                if "x-wealthsimple-otp" in response_headers and "required" in response_headers["x-wealthsimple-otp"]:
                                    self.login_status = "OTP"
                                    return self.login_status
                                else:
                                    self.login_status = "BAD_CREDS"
                                    return self.login_status
                time.sleep(1)
        self.login_status = "UNKNOWN,BAD_CREDS"
        return self.login_status
    
    def otp(self, otp, duration=30, repeat=1):
        for _ in range(repeat):
            start_time = time.time()
            self._login_otp(otp, duration=duration)
            # main purpose is to capture the bearer token
            print(f"Capturing network logs for {duration} seconds...")
            while time.time() - start_time < duration:
                logs = self.driver.get_log('performance')
                for entry in logs:
                    log = json.loads(entry['message'])['message']
                    if 'Network.responseReceived' in log['method'] and "params" in log and 'response' in log['params']:
                        response = log['params']['response']
                        if 'url' in response and response['url'].endswith('token'):
                            print(f"Network log: {json.dumps(log,indent=4)}")
                            try:
                                response_body = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
                                if response_body['base64Encoded']:
                                    response_body['body'] = base64.b64decode(response_body['body']).decode('UTF-8')                               
                                response_body = json.loads(response_body['body'])
                            except Exception:
                                response_body = {}
                            print(f"Body: {json.dumps(response_body, indent=4)}")
                            print("="*80)
                            if "access_token" in response_body:
                                # no need for otp, logged in
                                # update bearer token
                                self.bearer_token = response_body["access_token"]
                                self.login_status = "OK"
                                return self.login_status
                            elif "error" in response_body and "headers" in response:
                                response_headers = response['headers']
                                if "x-wealthsimple-otp" in response_headers and "invalid" in response_headers["x-wealthsimple-otp"]:
                                    self.login_status = "BAD_OTP"
                                    return self.login_status
                time.sleep(1)
        self.login_status = "UNKNOWN,BAD_OTP"
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

    # ====================================================================================================
    # mimic web activity
    # ====================================================================================================

    def mimic_webactivity(self):
        # mimic web activity
        # this is to prevent the website from logging us out
        self.scrape_bearer_token()
        time.sleep(3) # for sleep a couple seconds before trying to click around
        # click on a random element out of a list of elements
        target_number_of_clicks = random.randint(1, 5)
        failed_clicks = 0
        target_buttons = random.sample(self.safe_webactivity_buttons, target_number_of_clicks)
        for each in target_buttons:
            if self.driver.current_url != self.url_home:
                break
            try:
                self.driver.find_elements(By.XPATH, xpath_buttons_on_homepage)[each].click()
                time.sleep(0.5)
            except:
                failed_clicks += 1
        print(f"\nClicked {target_number_of_clicks - failed_clicks} out of {target_number_of_clicks} buttons: {target_buttons}")
        return
    
    def get_next_webactivity_time(self):
        return random.randint(1,3) * 45  # Random interval in seconds
    
    def thread_keep_alive(self, start=True):
        # chron job every n minutes to mimic web activity
        # use a simple threading.Timer to do this
        self.mimic_webactivity()
        next_interval = self.get_next_webactivity_time()
        print(f"Next mimic_webactivity scheduled in {next_interval} seconds.")
        threading.Timer(next_interval, self.thread_keep_alive).start()


    # ===================================================================================================================
    # Low level WS API
    # ===================================================================================================================
    import curls.curl_modify as curl_modify

    def send_request(self, curl, variables_input=None, json_data=None):
        default_url = 'https://my.wealthsimple.com/graphql'
        bearer_token = self.bearer_token

        # update the headers with the bearer token
        headers = curl.headers
        headers["authorization"] = bearer_token
        # get the json data
        if type(variables_input) is dict:
            # update the variables with the variables
            json_data = curl.json_data
            for key in variables_input:
                json_data['variables']['input'][key] = variables_input[key]
        # the user can also pass in the json_data directly
        # however, the variables_input will take precedence
        if json_data is None:
            json_data = curl.json_data
        # send the request
        url = default_url
        if hasattr(curl, "url"):
            url = curl.url
        response = requests.post(url, headers=headers, json=json_data, cookies=curl.cookies)
        if response.status_code == 401:
            print("*********** Authorization failed, reauthorize by using scrape_bearer_token **************")
        elif response.status_code != 200:
            print("*********** Request failed, error code: "+str(response.status_code)+" **************")
            print("Response: "+json.dumps(response.json(), indent=4))
        else:
            response_json_str = json.dumps(response.json(), indent=4)
            if '"errors": []' not in response_json_str and '"errors": null' not in response_json_str and '"errors":' in response_json_str:
                """
                Example 200 response with errors:
                {
                    "data": {
                        "soOrdersCreateOrder": {
                            "errors": [
                                {
                                    "code": "order.limit_price_outside_limit_threshold",
                                    "message": "Limit buy failed passive validation: limit=0.1 lastPrice=9.5450 lowerLimit=0.190900",
                                    "__typename": "SoOrders_ErrorResponse"
                                }
                            ],
                            "order": None,
                            "__typename": "SoOrders_CreateOrderTransformedResponse"
                        }
                    }
                }
                Example without errors:
                {
                    "data": {
                        "soOrdersModifyOrder": {
                            "errors": [],
                            "__typename": "SoOrders_ModifyOrderTransformedResponse"
                        }
                    }
                }
                and
                {
                    "data": {
                        "soOrdersCreateOrder": {
                            "errors": null,
                            "order": {
                                "orderId": "order-00XceCr8DhE4",
                                "createdAt": "2025-01-08T03:24:26.957Z",
                                "__typename": "SoOrders_OrderTransformedResponse"
                            },
                            "__typename": "SoOrders_CreateOrderTransformedResponse"
                        }
                    }
                }

                """
                print("*********** Request 200 but has WS error, status code: "+str(response.status_code)+" **************")
                print("Response: "+json.dumps(response.json(), indent=4))
                response.status_code = 200.5 # we will use this to indicate that the request was successful but had errors

        return response
    
    # ===================================================================================================================
    # High level WS API
    # ===================================================================================================================

    def modify_order(self, order_id, new_price):
        response = self.send_request(curl_modify, variables_input={"externalId": order_id, "newLimitPrice": new_price})
        return response
    
    def create_order(self, symbol, quantity, price, side):
        raise NotImplementedError
    
    def cancel_order(self, order_id):
        reponse = self.send_request(curl_cancel, variables_input={"externalId": order_id})

    def get_activity(self):
        raise NotImplementedError