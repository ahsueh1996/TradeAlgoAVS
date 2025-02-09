from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

def get_driver():
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--start-maximized")  # Optional: Start browser maximized
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    # Download here https://googlechromelabs.github.io/chrome-for-testing/
    if sys.platform == "darwin":
        path = "/app/wealthsimple-core/wspy/chromedriver-mac-arm64/chromedriver"
    elif "win" in sys.platform and sys.platform != "darwin":
        path = "/app/wealthsimple-core/wspy/chromedriver-win64/chromedriver.exe"
    elif "linux" in sys.platform:
        path = "/app/wealthsimple-core/wspy/chromedriver-linux64/chromedriver"
    print(f"Platform: {sys.platform}")
    print(f"Using chromedriver at: {path}")
    print(f"Checking if chromedriver exists: {os.path.exists(path)}")
    service = Service(executable_path=path)  # Update path to chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_driver_docker():
    # Set up Selenium WebDriver
    os.environ["DISPLAY"] = ":99"
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")  # Required in Docker
    options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Avoid GPU-related errors
    # options.add_argument("--user-data-dir=/tmp/chrome-user-data-unique-12345")  # Set a unique profile directory
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    # Download here https://googlechromelabs.github.io/chrome-for-testing/
    if sys.platform == "darwin":
        path = "/app/wealthsimple-core/wspy/chromedriver-mac-arm64/chromedriver"
    elif "win" in sys.platform and sys.platform != "darwin":
        path = "/app/wealthsimple-core/wspy/chromedriver-win64/chromedriver.exe"
    elif "linux" in sys.platform:
        path = "/app/wealthsimple-core/wspy/chromedriver-linux64/chromedriver"
    print(f"Platform: {sys.platform}")
    print(f"Using chromedriver at: {path}")
    print(f"Checking if chromedriver exists: {os.path.exists(path)}")
    print(f"*********Using docker options... ***********")
    service = Service(executable_path=path)  # Update path to chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_driver_docker_no_binary():
    os.environ["DISPLAY"] = ":99"
    print(f"Platform: {sys.platform}")
    print(f"Using chromedriver without specifying binary ... the docker way... ")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")  # Required in Docker
    options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Avoid GPU-related errors
    # options.add_argument("--user-data-dir=/tmp/chrome-user-data-unique-5647382")  # Set a unique profile directory
    driver = webdriver.Chrome(options=options)
    return driver


class TestSelenium:
    def __init__(self):
        self.url_login = "https://www.google.com"
        self.driver = None

    def test(self):
        try:
            self.driver = get_driver()
            print("Current session is {}".format(self.driver.session_id))
            self.driver.get(self.url_login)
        except Exception as e:
            print(f"Error: {e}")
            print("===========1=========="*4)
            print("Trying to use docker way...")
            try:
                self.driver = get_driver_docker()
                print("Current session is {}".format(self.driver.session_id))
                self.driver.get(self.url_login)
            except Exception as e:
                print(f"Error: {e}")
                print("===========2=========="*4)
                print("Trying to use unspecified driver...")
                try:
                    self.driver = get_driver_docker_no_binary()
                    print("Current session is {}".format(self.driver.session_id))
                    self.driver.get(self.url_login)
                except Exception as e:
                    print(f"Error: {e}")
                    print("Could not start webdriver, exiting...")
                    raise Exception("Could not start webdriver, exiting...")
        print("Success: Started webdriver...")

if __name__ == "__main__":
    test = TestSelenium()
    test.test()