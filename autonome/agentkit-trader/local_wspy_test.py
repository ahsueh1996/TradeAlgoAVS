from wspy import Client
from dotenv import load_dotenv
import os

load_dotenv()

WS_EMAIL = os.environ.get("WS_EMAIL")
WS_PASSWORD = os.environ.get("WS_PASSWORD")

client = Client()
while client.login_status != "OK":
    action = input("Action: ")
    if action == "login":
        client.login(WS_EMAIL, WS_PASSWORD)
    elif len(action) == 6 and action.isnumeric():
        client.otp(action)
    print("Login Status: "+client.login_status)

print("Starting thread to keep alive...")
client.thread_keep_alive(start=True)

input("End of test... (enter to exit)...")