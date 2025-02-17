from wspy import Client
from dotenv import load_dotenv
import os

load_dotenv()

WS_EMAIL = os.environ.get("WS_EMAIL")
WS_PASSWORD = os.environ.get("WS_PASSWORD")
try:
    WS_BEARER = os.environ.get("WS_BEARER")
    print("Found Bearer")
    WS_SESSION_COOKIE = os.environ.get("WS_SESSION_COOKIE")
    print("Found Session Cookie")
except:
    WS_BEARER = None

client = Client()
if WS_BEARER:
    client.open_authenticated_window(WS_BEARER, WS_SESSION_COOKIE)

input("Check for pre-authenticated window. Press enter to continue...")
if client.login_status != "OK":
    client.login(WS_EMAIL, WS_PASSWORD)

while client.login_status != "OK":
    action = input("Action: ")
    if action == "login":
        client.login(WS_EMAIL, WS_PASSWORD)
    elif len(action) == 6 and action.isnumeric():
        client.otp(action)
    print("Login Status: "+client.login_status)

print("Starting thread to keep alive...")
client.thread_keep_alive(start=True)

while True:
    action = input("Action: ")
    if action == "end":
        break
    elif action == "modify":
        order_id = input("Order ID: ")
        new_price = input("New Price: ")
        client.send_request(client.curl_modify, variables_input={"externalId": order_id, "newLimitPrice": new_price})

input("End of test... (enter to exit)...")