import requests

URL = "http://localhost:3000/chat"

def send_message(message):
    payload = {"data": message}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()  # Assuming the server responds with JSON
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = send_message(user_input)
        print("Bot:", response)
