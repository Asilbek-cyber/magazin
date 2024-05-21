import requests

def send_message(text):
    url = f"https://api.telegram.org/bot6961503071:AAGDxwQKafQZS89CtHAbiIOc2Ces-wckukk/sendMessage"
    params = {"chat_id": '882056073', "text": text}
    response = requests.post(url, data=params)
    return response.json()
